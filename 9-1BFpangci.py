import time

import pyautogui


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
            while pyautogui.locateCenterOnScreen(img, confidence=0.9) is not None:
                # print('没点上，再点一下')
                pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2,
                                button="left")
            break
    return picture_location


# 9-1炸鱼，sl 5鱼阵容，BF两点
def boom_fish(num, pangci):
    # 图片路径
    path_dir = 'pictures/9-1'

    # 点击地图
    point = click_picture(f'{path_dir}/map.png')

    # 点击出征
    click_picture(f'{path_dir}/go.png')
    time.sleep(1)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")

    # 等待阵容刷出
    while pyautogui.locateCenterOnScreen(f'{path_dir}/go_home.png', confidence=0.9) is None:
        time.sleep(0.1)

    # 判断是否是合适阵容
    if pyautogui.locateCenterOnScreen(f'{path_dir}/five_fish.png', confidence=0.9) is None:
        click_picture(f'{path_dir}/go_home.png')
        print('非5鱼阵容')
        return num, pangci
    else:
        # B点开炸
        click_picture(f'{path_dir}/start.png')
        click_picture(f'{path_dir}/danheng.png')

        # 结算
        point = click_picture(f'{path_dir}/come_on.png')
        time.sleep(1)
        pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(1)
        pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")

        # F点
        point = click_picture(f'{path_dir}/qianjin.png')
        time.sleep(1)
        pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
        # 可能锁不到敌
        while pyautogui.locateCenterOnScreen(f'{path_dir}/danheng.png', confidence=0.9) is None:
            if pyautogui.locateCenterOnScreen(f'{path_dir}/start.png', confidence=0.9) is None:
                time.sleep(0.1)
            else:
                break

        if pyautogui.locateCenterOnScreen(f'{path_dir}/danheng.png', confidence=0.9) is None:
            pass
        else:
            click_picture(f'{path_dir}/danheng.png')

            # 结算
            point = click_picture(f'{path_dir}/come_on.png')
            time.sleep(1)
            pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
            time.sleep(1)
            pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")

            # 回港
            click_picture(f'{path_dir}/finish.png')
            print('炸完惹')
            return num + 2, pangci

        # 检查是否有胖次
        if pyautogui.locateCenterOnScreen(f'{path_dir}/pangci.png', confidence=0.9) is None:
            print('没有胖次')
            click_picture(f'{path_dir}/go_home.png')
            return num + 1, pangci
        else:
            click_picture(f'{path_dir}/start.png')

        click_picture(f'{path_dir}/danheng.png')

        # 结算
        point = click_picture(f'{path_dir}/come_on.png')
        time.sleep(1)
        pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(1)
        pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")

        # 回港
        click_picture(f'{path_dir}/finish.png')
        print('炸完惹')
        return num + 2, pangci + 1


if __name__ == '__main__':
    i = 0
    p = 0
    while True:
    # while i < 22:
    # while p < 2:
        # while (i < 35) and (p < 21):
        i, p = boom_fish(i, p)
        print(f"已完成{i}次炸鱼，出了{p}条胖次")
    # print("over")
