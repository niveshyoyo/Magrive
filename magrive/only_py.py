#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import os
import time
import requests
import smtplib


def send_mail(shared_link, email, file):
    pass
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('magrive.io@gmail.com','ygovmebauxhtuddg')
    subject = 'MAGRIVE: '+file
    body = 'Link to your file: ' + shared_link
    msg = "Subject: {subject}\n\n{body}".format(**locals())

    server.sendmail('magrive.io@gmail.com',email,msg)

    print('email sent')

    server.quit()

def process_link(magnet_link, email_id):
    folder_upload_prefix = 'gdrive upload -p 1jT02vveuX7IcN_GyZN_eZiWcyIOAlWI8 -r data/'
    file_upload_prefix = 'gdrive upload -p 1jT02vveuX7IcN_GyZN_eZiWcyIOAlWI8 --share data/'


    folder_share_prefix = 'https://drive.google.com/open?id='
    file_share_prefix = 'https://drive.google.com/file/d/'


    # In[42]:
    # magnet_link = '''magnet:?xt=urn:btih:b3814200daedc2f3a607172ebee23d0671513c70&dn=www.TamilMV.bid%20-%20Mission%20Mangal%20(2019)%20Hindi%c2%a0Proper%20TRUE%20WEB-DL%20-%20720p%20-%20AVC%20-%20UNTOUCHED%20-%20AAC%20-%20600MB%20-%20ESub.mp4&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.pirateparty.gr%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2fopen.demonii.si%3a1337%2fannounce&tr=udp%3a%2f%2fipv4.tracker.harry.lu%3a80%2fannounce&tr=udp%3a%2f%2ftw.opentracker.ga%3a36920%2fannounce&tr=udp%3a%2f%2fdenis.stalker.upeer.me%3a6969%2fannounce&tr=http%3a%2f%2ft.nyaatracker.com%3a80%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fbt.xxx-tracker.com%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.vanitycore.co%3a6969%2fannounce&tr=http%3a%2f%2ftracker.city9x.com%3a2710%2fannounce&tr=udp%3a%2f%2ftracker.internetwarriors.net%3a1337%2fannounce'''
    # email_id = 'elusnehith@gmail.com'

    os.system('aria2c --seed-time=0.0 --dir="data/" "' + magnet_link + '"')
    os.system('rm data/*.torrent')

    file = os.listdir('data')
    is_folder = False

    if os.path.isdir('data/' + file[0]):
        is_folder = True
    print(is_folder)


    # In[44]:


    if is_folder:
        os.system(folder_upload_prefix + '"' + file[0] + '"')
        os.system('rm out.csv')
        os.system('''sudo gdrive list --query "'1jT02vveuX7IcN_GyZN_eZiWcyIOAlWI8' in parents" >> out.csv''')
        li = pd.read_csv('out.csv', delimiter='   ')
        cols = list(li.columns)
        a = np.array(li.loc[:,cols[0]:cols[1]])
        
        fold_id = a[0][0]

        
        os.system('gdrive share ' + fold_id)
        
        share_link = folder_share_prefix + fold_id
        print(share_link)
    else:
        os.system('rm out.csv')
        print(file_upload_prefix + '"' + file[0] + '" > out.csv')
        os.system(file_upload_prefix + '"' + file[0] + '" > out.csv')
        li = pd.read_csv('out.csv', delimiter = ' ')
        print(li.head())
        file_id = li.loc[0,list(li.columns)[1]]
        share_link = file_share_prefix + file_id
        print(share_link)

    send_mail(share_link, email_id, file[0])
    os.system('rm -r data/*')
    return share_link



# In[ ]:




