# thingino-webcam-monitor            
updated: 8/23/2026

Web browser webcam preview monitor.  For use with Thingino firmware potocol. 
This is a quick project that targets to bring all the camera that uses thingino firmware preview at one web page.  It will allow monitoring (and control) the cameras all at one place.  The quick camera site access also allow to fine tune the camera via web UI. 

## Features:
-  supports Prudynt-T streamer only
-  multiple camera preview (up to 16)
-  variable number of preview pans
-  variable number of viewing columns
-  flixible MJPEG camera channel access, including for the multi-sensor cameras.
-  full preview with a single click on a preview pan
-  access the camera site with a double click on a preview pan
-  download the snapshot of preview
-  motor control for the PTZ camera  
-  camera select and MJPEG URL input
-  save the camera URLs to the browser local storage
-  keyboard shortcut, useful in the full preview
-  can be ran from either a thingino camera or a independent web server
<img width="661" height="519" alt="monitor-4" src="https://github.com/user-attachments/assets/7a26580d-eda6-4a2f-9986-2952d7039095" />

(shown two units with two sensors each)

## Button Functions:  
### Layout control
<img width="145" height="43" alt="preview number" src="https://github.com/user-attachments/assets/3748f70a-66cd-4869-99c0-4117fdd94b3b" />  Select number of preview pans  

<img width="107" height="47" alt="display coumns" src="https://github.com/user-attachments/assets/62fdae0c-6663-4d6e-8701-851fffc4501c" />  Select number of preview pan in a row   


<img width="117" height="45" alt="save config" src="https://github.com/user-attachments/assets/dc996b6b-f8f5-4ee4-b4a1-253fce6d8b7a" />  Save configuration (URls)  

### Display and Site access
<img width="54" height="48" alt="full preview" src="https://github.com/user-attachments/assets/92167bc4-1b65-48c1-81c4-c722559fb8d4" />  Full preview for selected camera 

<img width="55" height="46" alt="camera site" src="https://github.com/user-attachments/assets/d2053e0e-bfd1-43d1-84e1-8b7d2ca16c29" />  To the selected camera web site  

<img width="50" height="45" alt="snapshot download" src="https://github.com/user-attachments/assets/315fab66-e6a6-4039-90d7-9abf157878e1" />  Download snapshot of selected preview  

<img width="296" height="67" alt="cam select" src="https://github.com/user-attachments/assets/f7e7132c-afd7-4014-bdd3-2d1aa4ad6320" />  Camera select (variable)  

### Motor control
<img width="170" height="92" alt="ptz control" src="https://github.com/user-attachments/assets/aac528e5-8ce9-4899-9b87-c59cbfff32b2" />  PTZ dirction control (H for home/calibrate)  

### Camera Function Control (need prudynt-t update and add www/x/json-prudynt-1.cgi)

<img width="50" height="76" alt="white-on-off" src="https://github.com/user-attachments/assets/0c8f7878-6a30-4670-ba0a-6aa264883b82" />  White Light on/off (direct JSON GPIO control in prudynt-t required)

<img width="48" height="79" alt="ir-on-off" src="https://github.com/user-attachments/assets/730f87c0-847e-423f-ae62-732bb344887a" />  IR Light on/off (direct JSON GPIO control in prudynt-t required)

<img width="48" height="80" alt="ir cut on-off" src="https://github.com/user-attachments/assets/89de6d8f-1e89-4e35-955c-9f60de232c0a" />  IR Cut on/off (direct JSON GPIO control in prudynt-t required)

<img width="51" height="76" alt="bw color" src="https://github.com/user-attachments/assets/ea57c430-f2d6-40a2-a045-c1ca0a60873c" />  Black and White / Color

<img width="52" height="81" alt="motio on-off" src="https://github.com/user-attachments/assets/b7d83161-a4ab-4105-99f1-a97c45f771f6" />  Motion Detection on/off

## Keyboard shortcuts:
- **\[up\]**:      motor up  
- **\[down\]**:    motor down  
- **\[left\]**:    motor left  
- **\[right\]**:   motor right  
- **1-9**:       camera select 1-9  
- **A-G(a-g)**:  camera select 10-16  
- **D(d)**:      download snapshot  
- **S(s)**:      camera site  

## Note:  
-  The "third party cookies" setting on web browser needs to enabled for the web server.
-  Each of the camera unit needs to be authenticated first for the image(s) to be access and stream.  If not prompted, access the camera web site first to trigger the authentication first.
-  The Camera Function Control is done by sending a JSON string through a new tab to the thingino web server (www/x/json-prudynt-1.cgi & prudyntctl).  This require enabling "allow pop up" in the web client settings at the camera sites.  It also require an escape character conversion (%22 to " ) be added in the thingino prudyntctl program on the camera firmware.  Otherwise, it won't process correctly.  

