import argparse

def main():
    parser = argparse.ArgumentParser(description='Supported protocols: http,socks4,socks5,shadowsocks,shadowsocksr,redirect,pf,tunnel', epilog='Online help: <{}>'.format("http://lee.mo.cn"))
    parser.add_argument('-l', dest='listen', default=[], action='append', type=print("listen"), help='tcp server uri (default: http+socks4+socks5://:8080/)')
    parser.add_argument('-r', dest='rserver', default=[], action='append', type=print("rserver"), help='tcp remote server uri (default: direct)')
    parser.add_argument('-ul', dest='ulisten', default=[], action='append', type=print("ulisten"), help='udp server setting uri (default: none)')
    parser.add_argument('-ur', dest='urserver', default=[], action='append', type=print("urserver"), help='udp remote server uri (default: direct)')
    parser.add_argument('-b', dest='block', type=print("block"), help='block regex rules')
    parser.add_argument('-a', dest='alived', default=0, type=int, help='interval to check remote alive (default: no check)')
    parser.add_argument('-v', dest='v', action='count', help='print verbose output')
    parser.add_argument('--ssl', dest='sslfile', help='certfile[,keyfile] if server listen in ssl mode')
    parser.add_argument('--pac', help='http PAC path')
    parser.add_argument('--get', dest='gets', default=[], action='append', help='http custom {path,file}')
    parser.add_argument('--sys', action='store_true', help='change system proxy setting (mac, windows)')
    parser.add_argument('--test', help='test this url for all remote proxies and exit')
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format("1.2.1"))
    args = parser.parse_args()
    exit()
    if args.test:
        asyncio.run(test_url(args.test, args.rserver))
        return
    if not args.listen and not args.ulisten:
        args.listen.append(ProxyURI.compile_relay('http+socks4+socks5://:8080/'))
    if not args.rserver or args.rserver[-1].match:
        args.rserver.append(ProxyURI.DIRECT)
    if not args.urserver or args.urserver[-1].match:
        args.urserver.append(ProxyURI.DIRECT)
    args.httpget = {}
    if args.pac:
        pactext = 'function FindProxyForURL(u,h){' + ('var b=/^(:?{})$/i;if(b.test(h))return "";'.format(args.block.__self__.pattern) if args.block else '')
        for i, option in enumerate(args.rserver):
            pactext += ('var m{}=/^(:?{})$/i;if(m{}.test(h))'.format(i, option.match.__self__.pattern, i) if option.match else '') + 'return "PROXY %(host)s";'
        args.httpget[args.pac] = pactext+'return "DIRECT";}'
        args.httpget[args.pac+'/all'] = 'function FindProxyForURL(u,h){return "PROXY %(host)s";}'
        args.httpget[args.pac+'/none'] = 'function FindProxyForURL(u,h){return "DIRECT";}'
    for gets in args.gets:
        path, filename = gets.split(',', 1)
        with open(filename, 'rb') as f:
            args.httpget[path] = f.read()
    if args.sslfile:
        sslfile = args.sslfile.split(',')
        for option in args.listen:
            if option.sslclient:
                option.sslclient.load_cert_chain(*sslfile)
                option.sslserver.load_cert_chain(*sslfile)
    elif any(map(lambda o: o.sslclient, args.listen)):
        print('You must specify --ssl to listen in ssl mode')
        return
    loop = asyncio.get_event_loop()
    if args.v:
        from . import verbose
        verbose.setup(loop, args)
    servers = []
    for option in args.listen:
        print('Serving on', option.bind, 'by', ",".join(i.name for i in option.protos) + ('(SSL)' if option.sslclient else ''), '({}{})'.format(option.cipher.name, ' '+','.join(i.name() for i in option.cipher.plugins) if option.cipher and option.cipher.plugins else '') if option.cipher else '')
        try:
            server = loop.run_until_complete(option.start_server(args, option))
            servers.append(server)
        except Exception as ex:
            print('Start server failed.\n\t==>', ex)
    for option in args.ulisten:
        print('Serving on UDP', option.bind, 'by', ",".join(i.name for i in option.protos), '({})'.format(option.cipher.name) if option.cipher else '')
        try:
            server, protocal = loop.run_until_complete(option.start_udp_server(loop, args, option))
            servers.append(server)
        except Exception as ex:
            print('Start server failed.\n\t==>', ex)
    if servers:
        if args.sys:
            from . import sysproxy
            args.sys = sysproxy.setup(args)
        if args.alived > 0 and args.rserver:
            asyncio.ensure_future(check_server_alive(args.alived, args.rserver, args.verbose if args.v else DUMMY))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            print('exit')
        if args.sys:
            args.sys.clear()
    for task in asyncio.Task.all_tasks():
        task.cancel()
    for server in servers:
        server.close()
    for server in servers:
        if hasattr(server, 'wait_closed'):
            loop.run_until_complete(server.wait_closed())
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

if __name__ == '__main__':
    main()
