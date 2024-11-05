import os
import shutil
import time
import requests
import io
from PIL import Image
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.common import ElementNotInteractableException
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from fake_headers import Headers


def automate_web_plot(image_name):
    """
        Opens WebPlotDigitizer and inserts an image from within the project
        :return:
        """
    # initializes driver and navigates to webplotdigitizer


    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://apps.automeris.io/wpd/")
    time.sleep(0.5)
    # clicks load image
    driver.find_element(By.ID, "start-sidebar")
    driver.find_element(By.XPATH, "//input[@value='Load Image']").click()
    time.sleep(0.5)
    # inserts image
    driver.find_element(By.ID, "loadNewImage")
    path = os.path.abspath(image_name)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(path)
    # clicks the next 2 confirm buttons
    driver.find_element(By.ID, "axesList")
    driver.find_element(By.XPATH, "//input[@value='Align Axes']").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "xyAxesInfo")
    driver.find_element(By.XPATH, "//input[@value='Proceed']").click()
    # options.remove_argument('--headless')
    time.sleep(1000)


def get_images(delay, max_images, keyword):
    # Define the name of the folder
    folder_name = "points"

    # Get the current working directory
    current_dir = os.getcwd()

    # Define the path to the folder
    folder_path = os.path.join(current_dir, folder_name)

    # Check if the folder already exists
    if os.path.exists(folder_path):
        # If the folder exists, delete its contents
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    else:
        # If the folder doesn't exist, create it
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            # If the folder already exists, delete its contents and try creating it again
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            os.mkdir(folder_path)
        # Define the name of the folder
    folder_name = "output_csv"

    # Get the current working directory
    current_dir = os.getcwd()

    # Define the path to the folder
    folder_path = os.path.join(current_dir, folder_name)

    # Check if the folder already exists
    if os.path.exists(folder_path):
        # If the folder exists, delete its contents
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    else:
        # If the folder doesn't exist, create it
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            # If the folder already exists, delete its contents and try creating it again
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            os.mkdir(folder_path)
        # Define the name of the folder
    folder_name = "output_png"

    # Get the current working directory
    current_dir = os.getcwd()

    # Define the path to the folder
    folder_path = os.path.join(current_dir, folder_name)

    # Check if the folder already exists
    if os.path.exists(folder_path):
        # If the folder exists, delete its contents
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    else:
        # If the folder doesn't exist, create it
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            # If the folder already exists, delete its contents and try creating it again
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            os.mkdir(folder_path)
    # options = Options()
    # TODO: clean up code and delete files in points whenever this is called
    download_directory = os.path.join(os.path.dirname(__file__), 'points')
    chrome_options = webdriver.ChromeOptions()
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate only Windows platform
        headers=False  # generate misc headers
    )
    customUserAgent = header.generate()['User-Agent']
    chrome_options.add_argument(f"user-agent={customUserAgent}")

    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': download_directory,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.campusplastics.com/")

    # # Search for the keyword and click the search button
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "onlinesearch"))
    )
    search_box.send_keys(keyword)
    time.sleep(3)
    # Find the form by its ID or other selector
    checkbox = driver.find_element(By.CSS_SELECTOR, "input[id*='cb']")
    driver.execute_script("arguments[0].click();", checkbox)
    # Click the checkbox
    # checkbox.click()
    # Search for the keyword and click the search button
    time.sleep(0.75)
    pinboard = driver.find_element(By.ID, "pinboard-add-all")
    time.sleep(0.75)
    driver.execute_script("arguments[0].scrollIntoView();", pinboard)
    time.sleep(0.75)
    driver.execute_script("arguments[0].click();", pinboard)
    time.sleep(0.75)
    pinboard.send_keys(Keys.TAB)
    hovered_element = driver.switch_to.active_element
    hovered_element.send_keys(Keys.TAB)
    hovered_element = driver.switch_to.active_element
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(hovered_element).key_up(Keys.CONTROL).perform()

    while hovered_element.get_attribute("id") != "cookiePrivacyPolicy":
        print(hovered_element.get_attribute("id"))
        hovered_element.send_keys(Keys.TAB)
        hovered_element = driver.switch_to.active_element
        if hovered_element.get_attribute("id") == "cookiePrivacyPolicy":
            break
        print(hovered_element.get_attribute("id"))
        hovered_element.send_keys(Keys.TAB)
        hovered_element = driver.switch_to.active_element
        actions.key_down(Keys.CONTROL).click(hovered_element).key_up(Keys.CONTROL).perform()
    tab_handles = driver.window_handles

    # Switch to the second tab
    for i in range(len(tab_handles)):
        driver.switch_to.window(tab_handles[i])
        try:
            time.sleep(0.5)
            origin = driver.find_element(By.XPATH, '//div[@class="noUi-handle noUi-handle-lower"]')
            ActionChains(driver).click_and_hold(origin).move_by_offset(300, 5).release().perform()
            # origin.click()
            time.sleep(0.75)
        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
            print("no first capcha")
        finally:
            try:
                plots = driver.find_elements(By.CLASS_NAME, "diagrambox")
            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                print("no graphs on this page")
            else:
                for plot in plots:
                    driver.execute_script("arguments[0].scrollIntoView();", plot)
                    time.sleep(0.75)
                    # driver.execute_script("arguments[0].click();", plot)
                    plot.click()
                    # Find the h5 element with the class "modal-title"
                    h5_element = driver.find_element(By.XPATH, "//h5[contains(@class, 'modal-title')]")

                    # Get the text within the h5 element
                    text = h5_element.text

                    # Print the text
                    print(text)
                    if "stress-strain" in h5_element.text.lower():
                        print("The text 'stress strain' is present in the h5 element")
                        # this used to work but now doesn't
                        link = driver.find_element(By.XPATH, "//a[@id='menuitem-toggleView']")
                        # click the link
                        ActionChains(driver).move_to_element(link).click().perform()

                        # link = WebDriverWait(driver, 2).until(
                        #     EC.element_to_be_clickable((By.ID, "menuitem-toggleView")))
                        # link.click()
                        time.sleep(0.75)
                        try:
                            # origin = driver.find_element(By.XPATH, '//div[@class="noUi-origin"]')
                            #the below one is the good one that always worked but isnt now
                            origin = driver.find_element(By.XPATH, '//div[@class="noUi-handle noUi-handle-lower"]')
                            #origin = driver.find_element(By.CLASS_NAME, 'noUi-handle noUi-handle-lower')
                            #origin.click()
                            # the below is the previously working line
                            ActionChains(driver).click_and_hold(origin).move_by_offset(180, 5).release().perform()
                            #ActionChains(driver).move_to_element(origin).click_and_hold(origin).move_by_offset(180, 5).release().perform()

                        except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                            print("second captcha not there")
                        finally:
                            try:
                                time.sleep(1)
                                # this worked before but now doesnt work
                                # xls = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a["
                                #                                                                                 "@id"
                                #                                                                                 "='menuitem "
                                #                                                                                 "-xlsExport']")))
                                # # click the link
                                xls = WebDriverWait(driver, 2).until(
                                    EC.element_to_be_clickable((By.ID, "menuitem-xlsExport")))
                                xls.click()
                                time.sleep(2)
                                # this worked before but doesnt now
                                # ActionChains(driver).move_to_element(xls).click().perform()
                            except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                                print("points didnt download for some reason")
                            finally:

                                close = WebDriverWait(driver, 2).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH,
                                         "//button[contains(@class, 'close') and contains(@class, 'close noprint')]"))
                                )
                                time.sleep(0.75)
                                try:
                                    #ActionChains(driver).move_to_element(close).click().perform()
                                    ActionChains(driver).move_to_element(close).perform()
                                    close.click()
                                except (NoSuchElementException, ElementNotInteractableException, TimeoutException):
                                    print("???????")

                        # if the exception is caught it leaves the plots for loop

                    else:
                        print("The text 'stress strain' is not present in the h5 element")

                        close = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located(
                                (By.XPATH, "//button[contains(@class, 'close') and contains(@class, 'noprint')]"))
                        )
                        time.sleep(0.5)
                        ActionChains(driver).move_to_element(close).click().perform()
            print("graph found")
        time.sleep(1)

    # time.sleep(3)
    # print("clicked")
    #
    # search_box = driver.find_element(By.NAME, "q")
    # search_box.send_keys(keyword)
    # search_box.submit()
    #
    # # Scroll down the page to load more images
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # while True:
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    #
    # # Find and download the images
    # image_url = set()
    # thumbnail = driver.find_elements(By.CLASS_NAME, "Q4LuWd")
    #
    # for img in thumbnail[len(image_url): max_images]:
    #     try:
    #         img.click()
    #         time.sleep(delay)
    #     except:
    #         continue
    #     images = driver.find_elements(By.CLASS_NAME, "n3VNCb")
    #     for image in images:
    #         if image.get_attribute('src') and 'http' in image.get_attribute('src'):
    #             image_url.add(image.get_attribute('src'))
    #             print(f"found image {len(image_url)}")
    #
    # # Download the images
    # for url in image_url:
    #     image_content = requests.get(url).content
    #     image_file = io.BytesIO(image_content)
    #     try:
    #         image = Image.open(image_file).convert('RGBA')
    #     except:
    #         print(f"Skipping image {url} due to error.")
    #         continue
    #     # Save the image to the 'images' folder
    #     filename = url.split("/")[-1].split("?")[0]
    #     # delete the folder to start fresh
    #     #     # TODO: make this work
    #     #     # shutil.rmtree("images")
    #     if not os.path.exists("images"):
    #         os.makedirs("images")
    #     with open(os.path.join("images", filename), "wb") as f:
    #         image.save(f, "PNG")

    # Close the Chrome window
    driver.quit()
