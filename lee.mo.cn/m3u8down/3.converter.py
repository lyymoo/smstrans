import os
import glob

root_dir = "Episodes/"
output_format = ".mkv"
overwrite = "-y" #leave blank if no, else, "-y"

def locate_playlist():
     for filename in glob.iglob(root_dir + '**/playlist.m3u8', recursive=True):
          folder_name = filename.split("\\")[-2]
          directory = "\\".join(filename.split("\\")[:-1])
          in_file = filename.split("\\")[-1:][0]
          out_file = "..\\"+folder_name+output_format
          if "Episode" in out_file:
               fancy_formatting = folder_name.split("Episode")
               fancy_formatting = fancy_formatting[0]+"- EP"+fancy_formatting[1].strip()
               out_file = "..\\"+fancy_formatting+output_format
          convert(directory,in_file,out_file)
          
def convert(directory, in_file, out_file):
     command = 'cd "'+directory+'" && ffmpeg '+overwrite+' -i "'+in_file+'" -acodec copy -bsf:a aac_adtstoasc -vcodec copy "'+out_file+'"'
     print(command)
     try:
         os.system(command)
     except:
         print("Something went wrong!")

locate_playlist()
