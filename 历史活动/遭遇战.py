import time

import pyautogui

pyautogui.FAILSAFE = False


# 点击图片
def click_picture(image_name):
    img = image_name
    while True:
        time.sleep(0.2)
        picture_location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # print(picture_location)
        # 未成功匹配则进行等待
        if picture_location is None:
            time.sleep(0.1)
            # print('未找到图片，续0.1s', image_name)
            # 成功匹配后直接点击
        else:
            pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            time.sleep(0.5)
            # while pyautogui.locateCenterOnScreen(img, confidence=0.9) is not None:
            #     # print('没点上，再点一下')
            #     pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2,
            #                     button="left")
            break
    return picture_location


# 9-1炸鱼，sl 5鱼阵容，BF两点
def boom_fish(num):
    # 图片路径
    path_dir = 'pictures/zaoyu'

    # 点击轻巡
    point = click_picture(f'{path_dir}/qingxun.png')

    # 点击出征
    click_picture(f'{path_dir}/go.png')
    time.sleep(1)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")


    click_picture(f'{path_dir}/start.png')
    click_picture(f'{path_dir}/danheng.png')

    # 结算
    click_picture(f'{path_dir}/come_on.png')
    time.sleep(1)
    while pyautogui.locateCenterOnScreen(f'{path_dir}/finish.png', confidence=0.9) is None:
        pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(0.5)

    # 回港
    click_picture(f'{path_dir}/finish.png')

    print('炸完惹')
    return num + 1


if __name__ == '__main__':
    i = 0
    # while True:
    while i < 200:
        i = boom_fish(i)
        print(f"已完成{i}次炸鱼")
