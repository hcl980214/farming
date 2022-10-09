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
            time.sleep(0.5)
            # print('未找到图片，续0.1s', image_name)
            # 成功匹配后直接点击
        else:
            pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            time.sleep(1)
            while pyautogui.locateCenterOnScreen(img, confidence=0.9) is not None:
                # print(img)
                # print('没点上，再点一下')
                pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2,
                                button="left")
            break
    return picture_location


# 8-2B航空点练级
def one_fighter_and_four_boss(num):
    # 图片路径
    path_dir = 'pictures/8-2'

    # 点击地图
    click_picture(f'{path_dir}/map.png')

    # 点击出征
    point = click_picture(f'{path_dir}/go.png')
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")


    # 选择战况  
    point = click_picture(f'{path_dir}/miaozhun.png')
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
    time.sleep(0.5)
    pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")

    # 开始战斗
    # 可能锁不到敌
    while pyautogui.locateCenterOnScreen(f'{path_dir}/tixing.png', confidence=0.9) is None:
        if pyautogui.locateCenterOnScreen(f'{path_dir}/start.png', confidence=0.9) is None:
            time.sleep(0.1)
        else:
            click_picture(f'{path_dir}/start.png')
    click_picture(f'{path_dir}/tixing.png')

    # 放弃追击
    click_picture(f'{path_dir}/forgive.png')

    # 结算
    while (pyautogui.locateCenterOnScreen(f'{path_dir}/finish.png', confidence=0.9) is None) and (
            pyautogui.locateCenterOnScreen(f'{path_dir}/map.png', confidence=0.9) is None):
        pyautogui.click(point.x, point.y, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(1)

    if pyautogui.locateCenterOnScreen(f'{path_dir}/finish.png', confidence=0.9) is not None:
        click_picture(f'{path_dir}/finish.png')

    print('炸完惹')
    return num + 1


if __name__ == '__main__':
    i = 0
    # while i < 300:
    while True:
        i = one_fighter_and_four_boss(i)
        print(f"已完成{i}次8-2")
        time.sleep(1)
