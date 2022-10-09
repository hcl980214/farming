import time, os

# import cv2
import pyautogui


# # 缩放图像
# def JReduce(image_name, m):
#     img = cv2.imread(image_name, -1)
#     height, width = img.shape[:2]
#     # 按照指定比例缩放图像
#     size = (int(width * m), int(height * m))
#     # 返回缩放后图像变量
#     shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
#     return shrink
#
#
# # 测试使用屏幕与截图屏幕的缩放比例
# def test_rate(img):
#     # 从1/10到10倍大小缩放图像进行测试，获取缩放比例
#     for i in range(100, 10000):
#         img_m = JReduce(img, i / 1000)
#         picture_location = pyautogui.locateCenterOnScreen(img_m, confidence=0.8)
#         print(i)
#         if picture_location is not None:
#             return i
#         else:
#             pass


# 点击图片
def click_picture(image_name, m):
    # # 按照比例缩放读取图片
    # img = JReduce(image_name, m / 1000)
    img = image_name
    i = 0
    while i <= 50:
        picture_location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
        # print(picture_location)
        # 未成功匹配则进行等待
        if picture_location is None:
            time.sleep(0.1)
            print('未找到图片，续0.1s', i , image_name)
            # 成功匹配后直接点击
            i = i + 1
        else:
            pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2, button="left")
            break


def try_talking(picture_rate):
    all_choice = os.listdir('pictures/world_tree/farm/')
    print(all_choice)
    i = 0
    while i <= 100:
        for p in all_choice:
            picture_location = pyautogui.locateCenterOnScreen(f'pictures/world_tree/farm/{p}', confidence=0.9)
            # print(picture_location)
            # 未成功匹配则进行等待
            if picture_location is None:
                # time.sleep(0.1)
                i = i + 1
                print(i)
            # 成功匹配后直接点击
            else:
                time.sleep(0.1)
                picture_location = pyautogui.locateCenterOnScreen(f'pictures/world_tree/farm/{p}', confidence=0.9)
                pyautogui.click(picture_location.x, picture_location.y, clicks=1, interval=0.2, duration=0.2,
                                button="left")
                i = 0


def farm_start(picture_rate):
    click_picture('pictures/world_tree/go/chufamaoxian.png', picture_rate)
    click_picture('pictures/world_tree/go/sijing.png', picture_rate)
    click_picture('pictures/world_tree/go/kaishibiaoyan.png', picture_rate)
    click_picture('pictures/world_tree/go/tiaoguobiandui.png', picture_rate)
    try_talking(picture_rate)
    click_picture('pictures/world_tree/run/II.png', picture_rate)
    click_picture('pictures/world_tree/run/zhijietuichu.png', picture_rate)
    click_picture('pictures/world_tree/run/queren.png', picture_rate)
    click_picture('pictures/world_tree/run/guanbi.png', picture_rate)


if __name__ == '__main__':
    # rate = test_rate('pictures/world_tree/ready/maoxian.png')
    rate = 1000
    click_picture('pictures/world_tree/ready/maoxian.png', rate)
    click_picture('pictures/world_tree/ready/shijieshu.png', rate)
    while True:
        picture_location = pyautogui.locateCenterOnScreen('pictures/world_tree/complete/jindu_max.png', confidence=0.9)
        if picture_location is None:
            farm_start(rate)
        else:
            print('刷完惹！！！！！')
            break