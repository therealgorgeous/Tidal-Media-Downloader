#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   turkish.py
@Time    :   2020/09/13
@Author  :   Gorgeous & shhade for hack & Mutlu ŞEN
@Version :   1.0
@Contact :   realmutlusen@gmail.com
@Desc    :   Yanlış çeviri ya da düzenleme için 'realmutlusen@gmail.com'a mail atabilirsiniz.   
'''

class LangTurkish(object):
    SETTING = "AYARLAR"
    VALUE = "VERİLER"
    SETTING_DOWNLOAD_PATH = "İndirme konumu:"
    SETTING_ONLY_M4A = ".mp4 uzantısı m4a'ya çevrilsin:"
    SETTING_ADD_EXPLICIT_TAG = "'Küfürlü' etiketi eklensin:"
    SETTING_ADD_HYPHEN = "Boşluk yerine '-' eklensin:"
    SETTING_ADD_YEAR = "Yıl eklensin:"
    SETTING_USE_TRACK_NUM = "Artist numarası eklensin:"
    SETTING_AUDIO_QUALITY = "Ses kalitesi:"
    SETTING_VIDEO_QUALITY = "Video kalitesi:"
    SETTING_CHECK_EXIST = "İndirilmiş mi diye kontrol edilsin:"
    SETTING_ARTIST_BEFORE_TITLE = "Artist adı eklensin:"
    SETTING_ALBUMID_BEFORE_FOLDER = "ID eklensin:"
    SETTING_INCLUDE_EP = "Single'ler ve EP'ler dahil edisin:"
    SETTING_SAVE_COVERS = "Albüm kapağı indirilsin:"
    SETTING_LANGUAGE = "Kullanılan lisan:"
    SETTING_USE_PLAYLIST_FOLDER = "Albümler klasör halinde indirilsin mi ?"
    SETTING_MULITHREAD_DOWNLOAD = "Şarkılar tek tek indirilsin mi?"
    SETTING_ALBUM_FOLDER_FORMAT = "Klasör ismi formatı:"
    SETTING_TRACK_FILE_FORMAT = "Dosya ismi formatı:"
    SETTING_SHOW_PROGRESS = "İndirme Çubuğu Görüntüleme:"

    CHOICE = "Seçim"
    FUNCTION = "İşlemler"
    CHOICE_ENTER = "Enter"
    CHOICE_ENTER_URLID = "'Url/ID' Gir:"
    CHOICE_EXIT = "Çıkış"
    CHOICE_LOGIN = "AccessToken'i Kontrol Et"
    CHOICE_SETTINGS = "Ayarlar'ı Düzenle"
    #CHOICE_SET_ACCESS_TOKEN = "'AccessToken' Gir"
    CHOICE_DOWNLOAD_BY_URL = "URL ya da ID ile indir"

    PRINT_ERR = "[HATA OLUŞTU]"
    PRINT_INFO = "[BİLGİ]"
    PRINT_SUCCESS = "[İNDİRİLDİ]"

    PRINT_ENTER_CHOICE = "Seçim Gir: "
    PRINT_LATEST_VERSION = "Mevcut Versiyon:"
    #PRINT_USERNAME = "Kullanıcı Adı ya da Mail Adresi:"
    #PRINT_PASSWORD = "Şifre:"

    CHANGE_START_SETTINGS = ">>> Ayarları düzenlemek istediğine emin misin ? ('0'-Geri Dön,'1'-Evet): "
    CHANGE_DOWNLOAD_PATH = ">>> İndirme konumu ('0' aynı kalsın): "
    CHANGE_AUDIO_QUALITY = ">>> Ses kalitesi ('0'-Normal,'1'-Yüksek,'2'-HiFi,'3'-[M]aster): "
    CHANGE_VIDEO_QUALITY = ">>> Video kalitesi ('0'-1080P,'1'-720P,'2'-480P,'3'-360P): "
    CHANGE_ONLYM4A = ">>> .mp4 uzantılı dosyalar .m4a'ya çevrilsin mi?('0'-Hayır,'1'-Evet): "
    CHANGE_ADD_EXPLICIT_TAG = ">>> 'Explicit' yani 'küfürlü' etiketi eklensin mi?('0'-Hayır,'1'-Evet): "
    CHANGE_ADD_HYPHEN = ">>> Şarkı dosyasının isminde boşluk yerine '-' eklensin mi ?('0'-Hayır,'1'-Evet): "
    CHANGE_ADD_YEAR = ">>> Albüm klasörünün isminde yıl olsun mu ?('0'-Hayır,'1'-Evet): "
    CHANGE_USE_TRACK_NUM = ">>> Şarkı dosyasının isminde albümdeki sırası yazsın mı ?('0'-Hayır,'1'-Evet): "
    CHANGE_CHECK_EXIST = ">>> Dosya daha önce indirilmiş mi diye kontrol edilsin mi ?('0'-Hayır,'1'-Evet): "
    CHANGE_ARTIST_BEFORE_TITLE = ">>> Şarkı dosyasının ismine sanatçının adı eklensin mi?('0'-Hayır,'1'-Evet): "
    CHANGE_INCLUDE_EP = ">>> Artist'in tüm albümlerini indirirken Single'leri ve EP'leri de dahil edilsin mi ?('0'-Hayır,'1'-Evet): "
    CHANGE_ALBUMID_BEFORE_FOLDER = ">>> Albüm klasörünün ismine ID eklensin mi ?('0'-Hayır,'1'-Evet): "
    CHANGE_SAVE_COVERS = ">>> Albüm kapağı indirilsin mi?('0'-Hayır,'1'-Evet): "
    CHANGE_LANGUAGE = ">>> Lisan Seç:"
    CHANGE_ALBUM_FOLDER_FORMAT = "Albüm klasörünün isim formatı('0' aynı kalsın):"
    CHANGE_TRACK_FILE_FORMAT = "Şarkı dosyalarının isim formatı('0' aynı kalsın):"
    CHANGE_SHOW_PROGRESS = "İndirme çubuğu görüntülensin mi?('0'-Hayır,'1'-Evet):"

    # {} are required in these strings
    AUTH_START_LOGIN = "Giriş işlemi başlatılıyor..."
    AUTH_LOGIN_CODE = "Giriş Kodunuz: {}"
    AUTH_NEXT_STEP = "{} bağlantısına gidip giriş yaptıktan sonra üstteki kodu giriniz. Lütfen {} dakika içerisinde tamamlayınız."
    AUTH_WAITING = "Giriş kodunu girmenizi bekliyoruz..."
    AUTH_TIMEOUT = "İşlem zaman aşımına uğradı, lütfen size verilen süre içerisinde işlemlerinizi gerçekleştiriniz!"
    
    MSG_VALID_ACCESSTOKEN = "AccessToken'iniz {} boyunca geçerlidir.."
    MSG_INVAILD_ACCESSTOKEN = "AccessToken süresi bitti. Yenileniyor..."
    MSG_PATH_ERR = "İndirme konumu ile alakalı bir sorun var! ('/storage/emulated/0/Download/' şeklinde girebilirsiniz.)"
    MSG_INPUT_ERR = "Giriş Hatalı!"

    MODEL_ALBUM_PROPERTY = "ALBÜM-BİLGİLERİ"
    MODEL_TRACK_PROPERTY = "ŞARKI-BİLGİLERİ"
    MODEL_VIDEO_PROPERTY = "VİDEO-BİLGİLERİ"
    MODEL_ARTIST_PROPERTY = "ARTİST-BİLGİLERİ"
    MODEL_PLAYLIST_PROPERTY = "OYNATMA LİSTESİ-BİLGİLERİ"

    MODEL_TITLE = 'Şarkı/Albüm Adı'
    MODEL_TRACK_NUMBER = 'Şarkı Sayısı'
    MODEL_VIDEO_NUMBER = 'Video Sayısı'
    MODEL_RELEASE_DATE = 'Çıkış Yılı'
    MODEL_VERSION = 'Versiyon'
    MODEL_EXPLICIT = 'Küfürlü'
    MODEL_ALBUM = 'Albüm'
    MODEL_ID = 'ID'
    MODEL_NAME = 'İsim'
    MODEL_TYPE = 'Türü'
