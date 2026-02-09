# coding = utf-8
import requests
import time
from lxml import etree
import os
import sys
from ncmdump import NeteaseCloudMusicFile
from pydub import AudioSegment  
import zipfile
import pyloudnorm
import soundfile
import shutil
import re


headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Cookie": "nts_mail_user=zz20080827@163.com:-1:1; _ntes_nnid=9b33c65da47d20622e5d53850166b5bc,1757754317396; _ntes_nuid=9b33c65da47d20622e5d53850166b5bc; NMTID=00OROGsuAAZFel4I0XegTVvIUCFHm0AAAGZQlJa5g; WEVNSM=1.0.0; WNMCID=ftozaf.1757754317621.01.0; sDeviceId=YD-AyPVJVlvz%2BlAFlBFABfWkmQZJgk9Q2Ew; WM_TID=yTx55plqzhFBARABBEOG13FJIgksF76k; __snaker__id=fJ6q6E0SuoKLD3uR; ntes_kaola_ad=1; NTES_CMT_USER_INFO=311320006%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0izBT6%7Chttps%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CenoyMDA4MDgyN0AxNjMuY29t; __remember_me=true; _iuqxldmzr_=32; NTES_P_UTID=rXOwFtQMDkNfnjTjz6i3zNR8vNtBsVvk|1763788251; P_INFO=szzxov@163.com|1763788251|0|music|00&99|jis&1763787855&music#jis&320500#10#0#0|&0|music|szzxov@163.com; MUSIC_U=002938BF0C2D9D1D9C23740D3CF0CADDEAB75EDB39CF847E529388BD660B2696E37D1DF037B9BCEFF1B6A84986C94BE669A9D3815643394DEB438D34AB93BA6954B8C01041B5A4DE53D724E77903DF1CCE73D0FF525F0313808A4484CF61C24998EAA3CFCFA33E49F7CCF99F5A16D776A5FB9C5B24A5BA44B4120A813954246FDDBCF6B6CD02879101E919817718CEA064F272E39B63BCADB83846941C6A5A17B0E624E25E25180A671E2597631DCA2A7B60C60C8AF51144C1C01047388DBECBD7743F66A642F82B39B85704BAD06AFA24109D753AE07E6A23BEB6E75B3E7144B694BE1073B65AD61CAD20E0A5EE978C954B4272465B21A44547393D1931EB2D0496F703BA28DF9DC9D9A7395C252CD0E77470A21A55E5F9E35016BB742A617F448F73AFDE50B1DBD52ADAF7A1F8411072985A1EF6A17AEEB2F59AC6066C9527E78702C78FBD5E1B039EF5F4FBC8F0A43F636DEBCD1F7DF8422AB97E6CF4BC780B02752397707E6C845D69D06BFC6CB16A38D947BB4A64699FA3D3FF22D35F05B2B50C43A27942790CDD5913CB98B8655A527BA009BB22CE45EF7CFB94541CE977; __csrf=e5d943115f56733624a1024b4d5a0c86; gdxidpyhxdE=L9GvsBzJI2ebytM6stPeHnmnnXVzdY%5CEm5VEf%5CjM6kuR7U96aKxIUNB6tjUuk5iGC8n8IJBDtlGxZ%2BqQUA9MmLzMfZn5PULNKoAVpXjKlstcDw8QV7cVeCfRme0%5CakhReW9GjbyBGGCuV5DCf5N3wOO%5CGesq%5C19Mm0X5EGL2sq9Cl7Cx%3A1763794613279; WM_NI=51eENgQflZMsR6AFoW0oKiWgYa0qzl%2FjecGXc62K0I%2FrcyN%2BJLQ%2BuG6nm76u8Lo2pQQnXcTPaYiORmPXVedrHmMIuGlHcxNXy%2B4Em7JnILQJMc3jhb1pkhdMt7KLi0vbWEo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb5ea61a3b0fca8ef6fae968fa2c55a938e8badc6738bb3bdafbc4ff6bfe188e22af0fea7c3b92af7efaba6cd6d93baa4bbd07992ea8fa7ee5df4b1858ad66d9bbf0092f968edb6ab84c654a1eafeacb343edaead9acd218a949fccf84df6b2a3d8b57ffc94a1d3f35b93b29884d75ca387a7b0d16794889a86e77a8cb383aaf84db098ad99cd54bbf5fca6f03d8ab287add4428fbdfd8beb6af3b0a589e747b8e985adec3cb6be99a6ee37e2a3; ntes_utid=tid._.EMEEkxzKcT9FVgFBAAPGgiRMIk08AiEl._.0.%2C.edd._.._.0; JSESSIONID-WYYY=d6Q5dSRkra4D8zEQQxqajOas8qwtdTsDK8aGk%2BP%2B9ieA%5C1okEFMGbbJFw53z%2BBJIt%2Fs1QnCkHNwK2rQ4F%2B45qr1inUOKXN1vnZ%2FYhnoO18mmOxuZlqDz%2F2uOkI9iKjp%2BY8aUj0A1Eu13%2FQ3lpCBrg9yjfeB4TXUAiQBo3calApFKINam%3A1763879890129",
    "Sec-Ch-Ua-Platform": "macOS",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1"}

authors = []    # 存放歌曲作者名字
names = []      # 存放歌曲名字
ids = []        # 存放歌曲的id
filenames = []  # 存放保存文件名
forbid = ['\\', '/', ':', '*', '?', r'"', '<', '>', '|']    # Windows中不合法的文件名

start_date = input('请输入开始放送的日期（YYYY/MM/DD）:')
playlist_id = input('请输入歌单id（可以直接复制链接）：')
playlist_id = re.findall(r'id=(\d+)', playlist_id)[0]   # 正则表达式过滤id
process_type = input('请输入处理类型（课间请输入break，宿舍输入dorm，午间输入noon）')
is_adding = int(input('如果有不在歌单中的歌曲，需要添加请填1，否则填0：'))

folder_name = start_date     # 懒得改了（
playlist_url = f'https://music.163.com/playlist?id={playlist_id}'    # 歌单的链接


def get_names_and_ids(url):    # 获取歌单中每一首歌的名字与id
    res = requests.get(url=url,headers=headers)
    res.encoding = 'utf-8'
    res_text = res.text
    html = etree.HTML(res_text)
    song_num = 0
    while True:
        song_num += 1
        try:
            id_ = html.xpath(f'//*[@id="song-list-pre-cache"]/ul/li[{song_num}]/a/@href')[0].replace('/song?id=', '')
        except IndexError:
            break
        name = html.xpath(f'//*[@id="song-list-pre-cache"]/ul/li[{song_num}]/a/text()')[0].replace('/song?id=', '')
        name = ''.join([i for i in name if i not in forbid])    # 去除非法字符
        ids.append(id_)
        names.append(name)
        
    print('ids:', ids)
    print('names:', names)

def get_authors():
    for id in ids:
        song_url = f'https://music.163.com/song?id={id}'
        res = requests.get(url=song_url,headers=headers)
        res.encoding = 'utf-8'
        res_text = res.text
        html = etree.HTML(res_text)
        author = html.xpath('/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/p[1]/span/*/text()')[:3]    # 文件保存时只取前三个作者名
        author = ','.join(author)   # 用逗号进行连接
        author = ''.join([i for i in author if i not in forbid])
        authors.append(author)
    print('authors:', authors)

def file_convert(index):     # 找到对应歌曲文件并转移到专用文件夹
    file_name = authors[index] + ' - ' + names[index]     # 生成文件名
    filenames.append(file_name)
    if not os.access(f"{file_name}.mp3", os.F_OK):    # 没有直接找到文件
        if not os.access(f"VipSongsDownload/{file_name}.ncm", os.F_OK):    # 非VIP曲库中的文件
            print('Error:找不到对应文件：', f"VipSongsDownload/{file_name}.ncm", '程序将自动退出')    # 有文件缺失 直接退出
            sys.exit()
        else:
            ncmfile = NeteaseCloudMusicFile(f"VipSongsDownload/{file_name}.ncm")
            ncmfile.decrypt()
            ncmfile.dump_music(f'{folder_name}/{file_name}.mp3')    # 将会员歌曲文件转换为可识别的格式
    else:
        shutil.move(f"{file_name}.mp3", f"{folder_name}/{file_name}.mp3")    # 移动文件到专用文件夹
    
def mp3_to_result_break(filename, index):   # 合成最终文件（课间）
    audio_file = AudioSegment.from_file(f'{folder_name}/{filename}.mp3', format='mp3')   # 读取对应音频文件
    if index == 0:
        save_name = '1.第一节课后'
    elif index == 1:
        save_name = '3.老校区第三节课后（东校区第六节课后）'
    elif index == 2:
        save_name = '5.第五节课后'
    elif index == 3:
        save_name = '7.第七节课后'    # 通过索引确定次序
    if len(audio_file) // 1000 > 290:
        audio_file = audio_file[:1000 * 290]
        audio_file = audio_file.fade_out(1000 * 30)     # 对于过长的音频进行删减
    if not os.path.exists(f'{folder_name}/results'):
        os.makedirs(f'{folder_name}/results')           # 创建相应的文件夹
    audio_file.export(f'{folder_name}/results/{save_name}' + '.wav', format='wav')
    normalization(f'{folder_name}/results/{save_name}' + '.wav')    # 电平标准化
    audio = AudioSegment.from_file(f'{folder_name}/results/{save_name}.wav', format='wav')
    audio.export(f'{folder_name}/results/{save_name}.mp3', format='mp3')   # 转换音频格式
    os.remove(f'{folder_name}/results/{save_name}.wav')     # 删除原有音频
    return f'{save_name}.mp3'    # 返回保存的名字

def normalization(filepath):    # 电平标准化
    data, rate = soundfile.read(filepath) # 加载音频
    # 峰值电平限制在-1.5dB
    peak_normalized_audio = pyloudnorm.normalize.peak(data, -1.5)
    # 首先测量响度
    meter = pyloudnorm.Meter(rate) # 创建 BS.1770 测量表
    loudness = meter.integrated_loudness(data)
    # 响度标准化至 -10dBFS
    loudness_normalized_audio = pyloudnorm.normalize.loudness(data, loudness, -10.0)
    soundfile.write(filepath, loudness_normalized_audio, rate)

def mp3_to_result_normal(save_name):
    audio = AudioSegment.silent(duration=4000)    # 创建空白音频
    for filename in filenames:
        audio_add = AudioSegment.from_file(f'{folder_name}/{filename}.mp3', format='mp3')
        audio = audio.append(audio_add, crossfade=3000)    # 将音频进行合成
    audio.export(f'{folder_name}/{save_name}.wav', format='wav')
    normalization(f'{folder_name}/{save_name}.wav')   # 电平标准化
    audio = AudioSegment.from_file(f'{folder_name}/{save_name}.wav', format='wav')
    audio.export(f'{folder_name}/{save_name}.mp3', format='mp3')# 转换音频格式
    os.remove(f'{folder_name}/{save_name}.wav')    # 删除原有音频


get_names_and_ids(playlist_url)
get_authors()
if is_adding == 1:
    length = int(input("请输入列表的长度："))

    # 循环输入每个元素
    for i in range(length):
        index_temp = int(input(f"请输入第 {i+1} 个歌曲位置（输入到最后请输入-1）："))
        name = input(f"请输入第 {i+1} 个歌曲名称：")
        author = input(f"请输入第 {i+1} 个歌手名称：")
        if index_temp == -1:
            index_temp = len(ids)     # insert()对于-1响应不当 故手动赋值
        ids.insert(index_temp, 0)     # 补充的音频id设置为0
        names.insert(index_temp, name)
        authors.insert(index_temp, author)
os.makedirs(folder_name)    # 创建相应的文件夹
for i in range(len(ids)):
    file_convert(i)
if process_type == 'noon':
    mp3_to_result_normal(f'{start_date}午间歌单')
elif process_type == 'dorm':
    mp3_to_result_normal(f'{start_date}宿舍歌单')
elif process_type == 'break':
    with zipfile.ZipFile(f'{start_date}课间歌单.zip', 'w') as myzip:   # 创建压缩包
        for i in range(len(ids)):
            saving = mp3_to_result_break(filenames[i], i)
            myzip.write(f'{folder_name}/results/' + saving, arcname=saving)   # 通过返回值写入文件名