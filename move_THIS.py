import os

def move_this(tongues_path):
    for root,dir,files in os.walk(tongues_path):
        for files in file:
            os.rename(f'{root}/{file}', f'final_img/{file}')

if __name__ == '__main__':
    move_this('tongues/unmarked/unmarked')
    move_this('tongues/marked/marked')