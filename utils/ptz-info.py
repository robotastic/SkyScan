import urllib.parse
import datetime
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPDigestAuth

class CameraConfiguration:
    """
    Module for configuration cameras AXIS
    """

    def __init__(self, ip, user, password):
        self.cam_ip = ip
        self.cam_user = user
        self.cam_password = password


    def get_info(self, url, payload={}):
        resp = requests.get(url, auth=HTTPDigestAuth(self.cam_user, self.cam_password),
                            params=payload)

        if resp.status_code == 200:
            return resp.text

        text = str(resp)
        text += str(resp.text)
        return text

    def get_ptz_config(self):  # 5.1.4
        url = 'http://' + self.cam_ip + '/axis-cgi/com/ptzconfig.cgi'
        return self.get_info(url)



    def get_image_source(self):  # 5.1.4
        url = 'http://' + self.cam_ip + '/axis-cgi/admin/param.cgi?action=list&group=ImageSource.I0.Sensor'
        return self.get_info(url)

    def get_position(self):  # 5.1.4
        payload = {'query': 'position'}
        #url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi?info=1'
        url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi'
        return self.get_info(url, payload)

    def get_limits(self):  # 5.1.4
        payload = {'query': 'limits'}
        #url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi?info=1'
        url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi'
        return self.get_info(url, payload)

    def get_ptz(self):
        url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi?info=1'
        return self.get_info(url)

    def set_iris_focus(self):
        """
        Enable or disable automatic iris control
        Args:
            iris: iris value (on, off)
        Returns:
            Success (OK) or Failure (Error and description).
        """
        payload = {
            'autoiris': 'off',
            'iris': 2500,
            'focus': 9999

        }

        url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi'
        resp = requests.get(url, auth=HTTPDigestAuth(self.cam_user, self.cam_password),
                            params=payload)

        if resp.status_code == 200:
            return resp.text

        text2 = str(resp)
        text2 += str(resp.text)
        return text2

    def set_focus(self):
        """
        Enable or disable automatic iris control
        Args:
            iris: iris value (on, off)
        Returns:
            Success (OK) or Failure (Error and description).
        """
        payload = {
            'focus': 9986

        }

        url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi'
        resp = requests.get(url, auth=HTTPDigestAuth(self.cam_user, self.cam_password),
                            params=payload)

        if resp.status_code == 200:
            return resp.text

        text2 = str(resp)
        text2 += str(resp.text)
        return text2



    def turn_on_auto_iris(self):
        payload = {
            'autoiris': 'on'
        }

        url = 'http://' + self.cam_ip + '/axis-cgi/com/ptz.cgi'
        resp = requests.get(url, auth=HTTPDigestAuth(self.cam_user, self.cam_password),
                            params=payload)

        if resp.status_code == 200:
            return resp.text

        text2 = str(resp)
        text2 += str(resp.text)
        return text2
ip = '192.168.1.74'
login = 'root'
password = 'admin'

cam = CameraConfiguration(ip, login, password)
#print(cam.auto_iris('on'))

#print(cam.set_iris_focus())
#print(cam.turn_on_auto_iris())
#print(cam.set_focus())
print(cam.get_position())
#print(cam.get_limits())
#9999 Focus, 5000 iris
#9999 focus, 3000 iris
#9999 focus, 2000 iris


# Shutter speed 1/1000
#pan=140.35
#tilt=63.55
#zoom=9999
#iris=1500
#focus=9983
#brightness=3499
#autofocus=off
#autoiris=off


#iris=3936
#focus=9962

#iris=2687
#focus=9999

#iris=1750
#focus=9961

#iris=2000
#focus=9999


#iris=2000
#focus=9951
#shutter 1/250

#iris=2000
#focus=9986
#shutter 1/250

#iris=2500
#focus=9975
#shutter 1/1000

#zoom=9597
#iris=2000
#focus=9941

#zoom=9999
#iris=2000
#focus=9925