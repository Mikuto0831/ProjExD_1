import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]
    # ここから 練習2
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    # ここから 練習8-1 rectの初期座標設定
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    # ここまで

    tmr = 0 # 時間保存

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() # 練習8-3 全キーの押下状態取得
        
        # 練習8-4 方向キーの押下状態を繁栄
        if key_lst[pg.K_UP]:
            kk_rct.move_ip(0,-1)
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip(0,1)
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip(-1,0)
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(1,0)
        


        # 練習7
        for i in range(4):
            screen.blit(bg_imgs[i%2], [-(tmr % 3200)+1600*i, 0])
         
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()