#!/usr/bin/env python3
#coding:utf-8
import os.path
import os
import click


@click.command()
@click.option('-s', prompt='源目录', help='源目录')
@click.option('-d', prompt='目标目录', help='目标目录')
def link(s, d):
    """目录硬链接创建工具。由于Linux 硬链接不支持目录，使用遍历创建目录，然后给文件创建硬链接。"""
    if not os.path.exists(s):
        print(s+"：源目录不存在！！！")
        return  - 1;

    if not os.path.exists(d):
        print("开始创建目录："+d)
        os.system("mkdir -p "+d)
    elif not len(os.listdir(d) ) == 0:
        print("目标目录 "+d+" 非空！！！")
        return -1;

    if not os.lstat(s).st_dev == os.lstat(d).st_dev:
        print("源目录和目标目录不在同一个磁盘！！！")
        #print("开始删除目录："+d)
        #os.system("rm -rvf "+d)
        print("程序退出！！！")
        return  -1 ;


    #目录末尾添加/用来后续拼接目录
    if not s.endswith("/"):
        s= s + "/"
    if not d.endswith("/"):
        d= d + "/"

    for parent,dirnames,filenames in os.walk(s):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in  dirnames:                       #输出文件夹信息
            cur_absolute_dir = os.path.join(parent, dirname)    #绝对路径
            cur_relative_dir = cur_absolute_dir.replace(s, ""); #相对路径

            print("源目录："+cur_absolute_dir)
            dst_dir = d + cur_relative_dir
            print("目标目录:"+dst_dir)

            print("开始创建目标目录："+dst_dir)
            os.system("mkdir -p \"" + dst_dir+"\"" )

        for filename in filenames:  # 输出文件信息
            cur_absolute_filename = os.path.join(parent, filename)
            cur_relative_filename = cur_absolute_filename.replace(s, "")

            # print("绝对路径："+cur_absolute_filename)  # 输出文件路径信息
            # print("相对路径："+cur_relative_filename)
            link_filename = d + cur_relative_filename
            print("开始创建硬链接: "+link_filename)
            link_cmd = "ln \""+cur_absolute_filename + "\"  \""+link_filename+"\""
            os.system(link_cmd)

if __name__ == '__main__':
    link()