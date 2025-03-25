import os
import simpe_functions
import glob
import picture_pdf
from jinja2 import Template
import html_temple as myhtml

def get_level_directories(root_dir):
    directories = []    
    # Получаем список содержимого корневой директории
    contents = os.listdir(root_dir)    
    # Фильтруем только те элементы, которые являются каталогами
    for item in contents:
        full_path = os.path.join(root_dir, item)
        if os.path.isdir(full_path):
            directories.append(item)            
    return directories  

def search_pdf(address):
    if os.path.exists(address+'/КТД на печать'):
        files = glob.glob(address+'/КТД на печать'+'/*.pdf', recursive=True) 
    else:
        files = glob.glob(address+'/*.pdf', recursive=True)
        # print(files)
    for i in files:
        if 'КМК' not in i.split('\\')[-1]:
            return i

if __name__ == "__main__":
    ls=[]
    root_directory = "src"
    level_directories = get_level_directories(root_directory)
    print(level_directories)
    for directory in level_directories:
        a=simpe_functions.search_folder('out\\',directory)
        if a :
            address_pdf_file=search_pdf(a)
            if address_pdf_file:      
                pic_link=os.path.join(root_directory,directory,"output.png")
                n=400
                picture_pdf.generate_thumbnail(address_pdf_file,pic_link, n*1.44, n)
                ls.append([directory,pic_link])
    print(ls)
    # Генерация HTML-страницы
    template = Template(myhtml.html_template)
    html_content = template.render(ls=ls)

    # Сохранение HTML-файла
    output_file = "protetica.html"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"HTML-каталог успешно создан: {output_file}")


    quit(-1)
    # for i in ls:
    #     if os.path.exists('out/'+i[0]):
    #         picture_pdf.create_pdf_from_images(i[0]+'\\'+i[1],'out/'+i[0])
    #     else:
        
            # print(b)

