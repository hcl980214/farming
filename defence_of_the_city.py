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
            print('未找到图片，续0.1s', image_name)
            # 成功匹配后直接点击
        else:
            pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            time.sleep(0.5)
            while pyautogui.locateCenterOnScreen(img, confidence=0.9) is not None:
                print('没点上，再点一下')
                pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2,
                                button="left")
            break


def defence_cycle():
    # 图片路径
    path_dir = 'pictures/defence_of_the_city'

    # 选择难度
    click_picture(f'{path_dir}/shoucheng.png')
    click_picture(f'{path_dir}/putongmoshi.png')
    click_picture(f'{path_dir}/putong.png')

    # 选择角色
    click_picture(f'{path_dir}/huli.png')
    click_picture(f'{path_dir}/queding.png')

    # 选择城门
    while pyautogui.locateCenterOnScreen(f'{path_dir}/fanye.png', confidence=0.9) is None:
        time.sleep(1)
    while pyautogui.locateCenterOnScreen(f'{path_dir}/chengmen.png') is None:
        picture_location = pyautogui.locateCenterOnScreen(f'{path_dir}/fanye.png', confidence=0.9)
        pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(0.2)
    click_picture(f'{path_dir}/chengmen.png')
    click_picture(f'{path_dir}/queding2.png')

    # 直接退出
    click_picture(f'{path_dir}/caidan.png')
    click_picture(f'{path_dir}/zhijietuichu.png')
    click_picture(f'{path_dir}/queren.png')
    click_picture(f'{path_dir}/guanbi3.png')

    # # 选择难度
    # click_picture(f'{path_dir}/shoucheng.png')
    # click_picture(f'{path_dir}/putongmoshi.png')
    # click_picture(f'{path_dir}/putong.png')
    #
    # # 选择角色
    # click_picture(f'{path_dir}/huli.png')
    # click_picture(f'{path_dir}/renyu.png')
    # click_picture(f'{path_dir}/queding.png')
    #
    # # 选择城门
    # while pyautogui.locateCenterOnScreen(f'{path_dir}/fanye.png', confidence=0.9) is None:
    #     time.sleep(1)
    # while pyautogui.locateCenterOnScreen(f'{path_dir}/chengmen.png', confidence=0.9) is None:
    #     picture_location = pyautogui.locateCenterOnScreen(f'{path_dir}/fanye.png', confidence=0.9)
    #     pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2, button="left")
    #     time.sleep(0.2)
    # click_picture(f'{path_dir}/chengmen.png')
    # click_picture(f'{path_dir}/queding2.png')
    #
    # # 配置角色
    # click_picture(f'{path_dir}/kaishizhandou.png')
    # click_picture(f'{path_dir}/1.png')
    # click_picture(f'{path_dir}/huli.png')
    # click_picture(f'{path_dir}/3.png')
    # click_picture(f'{path_dir}/renyu.png')
    #
    # # 第一轮
    # click_picture(f'{path_dir}/kaishibiaoyan.png')
    # click_picture(f'{path_dir}/shengli.png')
    # click_picture(f'{path_dir}/guanbi.png')
    #
    # # 第二轮
    # click_picture(f'{path_dir}/kaishizhandou.png')
    # click_picture(f'{path_dir}/kaishibiaoyan.png')
    # click_picture(f'{path_dir}/shengli.png')
    # click_picture(f'{path_dir}/guanbi.png')
    #
    # # 第三轮
    # click_picture(f'{path_dir}/kaishizhandou.png')
    # click_picture(f'{path_dir}/kaishibiaoyan.png')
    # click_picture(f'{path_dir}/guanbi2.png')


if __name__ == '__main__':
    while True:
        defence_cycle()