package cn.mo.lee.smstrans;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.telephony.SmsMessage;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.ArrayList;

/**
 * Created by moz on 2017/7/25.
 * Modified by moz on 2017/7/27.
 * Modified by moz on 2017/7/27. add some comment.
 */

public class TransmitReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Bundle bundle = intent.getExtras();
        SmsMessage msg = null;
        if (null != bundle) {
            Object[] smsObj = (Object[]) bundle.get("pdus");
            // 判断是否同一条短信
            String oldNumber = "";
            int i = 0;
            for (Object object : smsObj) {
                msg = SmsMessage.createFromPdu((byte[]) object);
                String newNumber = msg.getOriginatingAddress();
                if (newNumber.equals(oldNumber)){
                    i = i + 1;
                } else {
                    oldNumber = newNumber;
                }
            }
            // 转发的短信文本
            String allMsg = "";
            // 接收手机号（改成自己的手机号）
            String transmitNunmber = "18621971816";
            int j = 0;
            for (Object object : smsObj) {
                msg = SmsMessage.createFromPdu((byte[]) object);
                String number = msg.getOriginatingAddress();
                String message = msg.getDisplayMessageBody();
                // 过滤处理 包含特定字符串的短信不转发--开始
                /*  过滤 01 不转发流量提醒短信 */
                if (message.indexOf("您当月累计使用流量") != -1) {
                    continue;
                }
                // 过滤处理 包含特定字符串的短信不转发--结束
                if (i == 0) {
                    // 短信直接发送
                    message = number+" "+message;
                    if (transmitNunmber.equals("")){
                        Date date = new Date(msg.getTimestampMillis());
                        SimpleDateFormat format = new SimpleDateFormat("HH:mm:ss");
                        String receiveTime = format.format(date);
                    }else {
                        transmitMessageTo(transmitNunmber, message);
                    }
                } else {
                    // 短信拼接
                    j = j + 1;
                    if (j == 1) {
                        allMsg = number+" "+message;
                    } else {
                        allMsg = allMsg + message;
                    }
                }
            }
            // 短信拼接发送
            if (i > 0) {
                transmitMessageTo(transmitNunmber, allMsg);
            }
        }
    }

    public void transmitMessageTo(String phoneNumber,String message){
        SmsManager manager = SmsManager.getDefault();
        ArrayList<String> texts =manager.divideMessage(message);
        if (message.length() > 70) {
            manager.sendMultipartTextMessage(phoneNumber, null, texts, null, null);
        } else {
            for(String text:texts){
                manager.sendTextMessage(phoneNumber, null, text, null, null);
            }
        }
    }
}
