from django.shortcuts import render
from .forms import inputform
from .models import Mail
import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

#class Django 

def index(request):
    form = inputform()
    
    if request.method == "POST":
        url = request.POST.get('url')
        
        # check cache 
        cached = Mail.objects.filter(url=url).first()
        if cached:
            return render(request, 'send.html', {'words': cached.words, 'url': url})
        
        # proceceing 3 line 
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        words = ' '.join(p.get_text() for p in soup.find_all('p')).lower().split()
        word_count = Counter(w.strip(punctuation) for w in words if len(w.strip(punctuation)) > 1)
        
        #save and visualizing 
        Mail.objects.create(url=url, words=word_count.most_common())
        return render(request, 'send.html', {'words': word_count.most_common(), 'url': url})
    
    return render(request, 'home.html', {'form': form})


################################################################
# from django.shortcuts import render
# from .forms import inputform
# from .models import Mail
# import requests
# from bs4 import BeautifulSoup
# import re
# from collections import Counter

# def extract_key_sentences(text, num_sentences=4):
#     """
#     استخراج جملات کلیدی و مهم از متن (بدون نیاز به AI)
#     """
#     # تقسیم به جملات
#     sentences = re.split(r'(?<=[.!?])\s+', text)
    
#     # فیلتر جملات مفید (حداقل 40 و حداکثر 400 کاراکتر، بدون کلمات خاص)
#     valid_sentences = []
#     for sent in sentences:
#         sent = sent.strip()
#         # حذف جملات خیلی کوتاه، خیلی بلند، یا حاوی کاراکترهای خاص
#         if 40 < len(sent) < 400 and not sent.startswith(('#', '-', '*', '|')):
#             # حذف جملاتی که کلمات کلیدی مهم ندارند
#             if any(word in sent.lower() for word in ['authentication', 'token', 'user', 'api', 'docker', 'container', 'service', 'platform', 'linux', 'server', 'application', 'deploy', 'manage', 'config']):
#                 valid_sentences.append(sent)
    
#     # اگر با کلمات کلیدی چیزی پیدا نشد، از جملات اول استفاده کن
#     if len(valid_sentences) < 2:
#         valid_sentences = [s for s in sentences if 40 < len(s.strip()) < 400][:5]
    
#     # امتیازدهی بر اساس طول و کلمات مهم
#     important_words = ['authentication', 'authorization', 'token', 'user', 'permission', 'api', 'request', 
#                        'docker', 'container', 'image', 'kubernetes', 'cluster', 'service', 'deployment',
#                        'server', 'linux', 'ubuntu', 'centos', 'redhat', 'platform', 'infrastructure']
    
#     sentence_scores = []
#     for sent in valid_sentences:
#         score = 0
#         sent_lower = sent.lower()
#         for word in important_words:
#             if word in sent_lower:
#                 score += 3
#         # جملات خیلی کوتاه یا خیلی بلند جریمه شوند
#         word_count = len(sent.split())
#         if 15 < word_count < 40:
#             score += 2
#         sentence_scores.append((sent, score))
    
#     # انتخاب بهترین جملات
#     sentence_scores.sort(key=lambda x: x[1], reverse=True)
#     best_sentences = [sent for sent, score in sentence_scores[:num_sentences]]
    
#     # مرتب‌سازی بر اساس ترتیب اصلی در متن
#     ordered_sentences = [s for s in valid_sentences if s in best_sentences]
    
#     return ordered_sentences

# def get_page_text(url):
#     try:
#         # اضافه کردن User-Agent برای جلوگیری از بلاک شدن
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
#         response = requests.get(url, timeout=15, headers=headers)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # حذف المان‌های اضافی
#         for script in soup(["script", "style", "nav", "footer", "aside", "header", "meta", "link"]):
#             script.decompose()
        
#         # پیدا کردن محتوای اصلی
#         main_content = None
#         for selector in ['main', 'article', '.content', '.main-content', '#content', '.post-content', '.entry-content', 'body']:
#             main_content = soup.select_one(selector)
#             if main_content:
#                 break
        
#         if main_content:
#             text = main_content.get_text(separator=' ', strip=True)
#         else:
#             text = soup.get_text(separator=' ', strip=True)
        
#         # تمیز کردن متن: حذف فاصله‌های اضافی، خطوط خالی
#         text = re.sub(r'\s+', ' ', text)
#         text = re.sub(r'\n+', ' ', text)
#         text = text.strip()
        
#         return text
        
#     except requests.exceptions.RequestException as e:
#         return None
#     except Exception as e:
#         return None

# def index(request):
#     form = inputform()
    
#     if request.method == "POST":
#         url = request.POST.get('url')
        
#         page_content = get_page_text(url)
        
#         if not page_content:
#             answer = """ **خطا در دریافت محتوا**

# ممکن است دلایل زیر باعث این مشکل شده باشد:
# • اتصال اینترنت خود را بررسی کنید
# • وب‌سایت ممکن است موقتاً در دسترس نباشد
# • آدرس URL را مجدداً بررسی کنید

# لطفاً دوباره تلاش کنید."""
#         else:
#             # استخراج خلاصه هوشمند
#             summary_sentences = extract_key_sentences(page_content, num_sentences=4)
            
#             if summary_sentences:
#                 # ساخت خلاصه زیبا
#                 answer = " **خلاصه هوشمند از محتوای صفحه:**\n\n"
#                 for i, sentence in enumerate(summary_sentences, 1):
#                     # حذف فاصله‌های اضافی و لینک‌ها
#                     clean_sentence = re.sub(r'http\S+', '', sentence)
#                     clean_sentence = re.sub(r'\s+', ' ', clean_sentence).strip()
#                     answer += f"{i}. {clean_sentence}\n\n"
                
#                 # اضافه کردن اطلاعات آماری
#                 word_count = len(page_content.split())
#                 char_count = len(page_content)
#                 answer += f"---\n **آمار:** {word_count} کلمه | {char_count} کاراکتر | خلاصه از ۴ جمله کلیدی"
#             else:
#                 # اگر نتوانست خلاصه کند، اولین پاراگراف را نشان بده
#                 first_para = page_content.split('.')[:3]
#                 preview = '. '.join(first_para) + '.'
#                 answer = f" **پیش‌نمایش خودکار (امکان استخراج خلاصه نبود):**\n\n{preview}\n\n---\n💡 صفحه مورد نظر ساختار استانداردی ندارد."
        
#         # ذخیره در دیتابیس
#         Mail.objects.create(url=url, words=answer)
#         return render(request, 'send.html', {'words': answer, 'url': url})
    
#     return render(request, 'home.html', {'form': form})