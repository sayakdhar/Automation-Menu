#!/usr/bin/python36
import cgi
import subprocess as sp

print("content-type: text/html")
print()

print("""
<marquee> <font color="white"> <b> WELCOME TO FROST AUTOMATION TOOL </b> </font> </marquee>
""")
print("""
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}

/* Button used to open the contact form - fixed at the bottom of the page */
.open-button {
  background-color: #555;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  opacity: 0.8;
  position: fixed;
  bottom: 23px;
  right: 28px;
  width: 280px;
}

/* The popup form - hidden by default */
.form-popup {
  display: none;
  position: fixed;
  bottom: 0;
  right: 15px;
  border: 3px solid #f1f1f1;
  z-index: 9;
}

/* Add styles to the form container */
.form-container {
  max-width: 300px;
  padding: 10px;
  background-color: white;
}

/* Full-width input fields */
.form-container input[type=text], .form-container input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  border: none;
  background: #f1f1f1;
}

/* When the inputs get focus, do something */
.form-container input[type=text]:focus, .form-container input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Set a style for the submit/login button */
.form-container .btn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  margin-bottom:10px;
  opacity: 0.8;
}

/* Add a red background color to the cancel button */
.form-container .cancel {
  background-color: red;
}

/* Add some hover effects to buttons */
.form-container .btn:hover, .open-button:hover {
  opacity: 1;
}
</style>
</head>
<body>
""")
print("""<button class="open-button" onclick="openForm()" style="position:absolute;top:5%;left:40%;height:7%">Docker</button>

<div class="form-popup" id="myForm">
  <form action="" class="form-container">
    <h1>Docker</h1>

    <label for="email"><b>Docker Name</b></label>
    <input type="text" placeholder="Enter Docker Name" name="docker_name" required>

    <button type="submit" class="btn">Launch Docker</button>
    <button type="button" class="btn cancel" onclick="closeForm()">Cancel</button>
  </form>
</div>

<script>
function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
y=mydata.getvalue('docker_name')
x=sp.getstatusoutput("sudo ansible-playbook docker.yml --extra-vars name={}".format(y))
#if(x[0]==0):
#	import ctypes  # An included library with Python install.
#	def Mbox(title, text, style):
#		return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#	Mbox('Docker Notification', 'Docker Successfully Launch', 1)
#else:
#	print("<br>window.alert(Unsuccessful)")

print("""<button class="open-button" onclick="openForm1()" style="position:absolute;top:13%;left:40%;height:7%">Mail</button>

<div class="form-popup" id="myForm1">
  <form action="" class="form-container" method="POST">
    <h1>Mail</h1>

    <label for="email"><b>Sender's Address</b></label>
    <input type="text" placeholder="Enter Sender's mail" name="send_addr" required>

    <label fo r="email"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="password" required>

    <label for="email"><b>Recepient's Address</b></label>
    <input type="text" placeholder="Enter Recipient mail" name="rec_mail" required>

    <textarea rows='5' cols='30' name='msg' placeholder='Message'>
    </textarea>

    <label for="email"><b>Subject</b></label>
    <input type="text" placeholder="Enter Subject" name="subject" required>

    <button type="submit" class="btn">Send Mail</button>
    <button type="button" class="btn cancel" onclick="closeForm1()">Cancel</button>
  </form>
</div>

<script>
function openForm1() {
  document.getElementById("myForm1").style.display = "block";
}

function closeForm1() {
  document.getElementById("myForm1").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
a=mydata.getvalue('send_addr')
b=mydata.getvalue('password')
c=mydata.getvalue('rec_mail')
d=mydata.getvalue('msg')
e=mydata.getvalue('subject')
x=sp.getstatusoutput("sudo ansible-playbook mail.yml --extra-vars user_name={} --extra-vars Receiver={} --extra-vars passwrd={} --extra-vars sub={} --extra-vars message={}".format(a,c,b,e,d))

print("""<button class="open-button" onclick="openForm2()" style="position:absolute;top:21%;left:40%;height:7%">EC2 Instance</button>

<div class="form-popup" id="myForm2">
  <form action="" class="form-container">
    <h1>EC2 Instance</h1>

    <label for="email"><b>Access Key</b></label>
    <input type="password" placeholder="Enter Access key" name="access_key" required>

    <label for="email"><b>Secret Key</b></label>
    <input type="password" placeholder="Enter Secret key" name="secret_key" required>

    <button type="submit" class="btn">Launch EC2 Instance</button>
    <button type="button" class="btn cancel" onclick="closeForm2()">Cancel</button>
  </form>
</div>

<script>
function openForm2() {
  document.getElementById("myForm2").style.display = "block";
}

function closeForm2() {
  document.getElementById("myForm2").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
f=mydata.getvalue('access_key')
g=mydata.getvalue('secret_key')
x=sp.getstatusoutput("sudo ansible-playbook aws_ec2.yml --extra-vars access_key={} --extra-vars secret_key={}".format(f,g))
print("""<button class="open-button" onclick="openForm3()" style="position:absolute;top:29%;left:40%;height:7%">Web Service</button>

<div class="form-popup" id="myForm3">
  <form action="" class="form-container">
    <h1>Web Service</h1>

    <button type="submit" class="btn">Start Web Service</button>
    <button type="button" class="btn cancel" onclick="closeForm3()">Cancel</button>
  </form>
</div>

<script>
function openForm3() {
  document.getElementById("myForm3").style.display = "block";
}

function closeForm3() {
  document.getElementById("myForm3").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
x=sp.getstatusoutput("sudo ansible-playbook httpd.yml")

print("""<button class="open-button" onclick="openForm4()" style="position:absolute;top:37%;left:40%;height:7%">Bucket</button>

<div class="form-popup" id="myForm4">
  <form action="" class="form-container">
    <h1>Bucket</h1>

    <label for="email"><b>Access Key</b></label>
    <input type="password" placeholder="Enter Access key" name="access_key" required>

    <label for="email"><b>Secret Key</b></label>
    <input type="password" placeholder="Enter Secret key" name="secret_key" required>

    <label for="email"><b>Bucket Name</b></label>
    <input type="text" placeholder="Enter Bucket Name" name="bucket_name" required>

    <button type="submit" class="btn">Create Bucket</button>
    <button type="button" class="btn cancel" onclick="closeForm4()">Cancel</button>
  </form>
</div>

<script>
function openForm4() {
  document.getElementById("myForm4").style.display = "block";
}

function closeForm4() {
  document.getElementById("myForm4").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
h=mydata.getvalue('access_key')
i=mydata.getvalue('secret_key')
j=mydata.getvalue('bucket_name')
x=sp.getstatusoutput("sudo ansible-playbook bucket.yml --extra-vars access_key={} --extra-vars secret_key={} --extra-vars bucketname={}".format(h,i,j))

print("""<button class="open-button" onclick="openForm5()" style="position:absolute;top:45%;left:40%;height:7%">Directory</button>

<div class="form-popup" id="myForm5">
  <form action="" class="form-container">
    <h1>Directory</h1>

    <label for="email"><b>Path</b></label>
    <input type="text" placeholder="Ex:/root/Deskop/" name="path" required>

    <button type="submit" class="btn">Create Directory</button>
    <button type="button" class="btn cancel" onclick="closeForm5()">Cancel</button>
  </form>
</div>

<script>
function openForm5() {
  document.getElementById("myForm5").style.display = "block";
}

function closeForm5() {
  document.getElementById("myForm5").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
k=mydata.getvalue('path')
x=sp.getstatusoutput("sudo ansible-playbook folder.yml --extra-vars path2={}".format(k))

print("""<button class="open-button" onclick="openForm6()" style="position:absolute;top:53%;left:40%;height:7%">File</button>

<div class="form-popup" id="myForm6">
  <form action="" class="form-container">
    <h1>Directory</h1>

    <label for="email"><b>Path</b></label>
    <input type="text" placeholder="Ex:/root/Deskop/file_name.ext" name="path1" required>

    <button type="submit" class="btn">Create File</button>
    <button type="button" class="btn cancel" onclick="closeForm6()">Cancel</button>
  </form>
</div>

<script>
function openForm6() {
  document.getElementById("myForm6").style.display = "block";
}

function closeForm6() {
  document.getElementById("myForm6").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
l=mydata.getvalue('path1')
x=sp.getstatusoutput("sudo ansible-playbook file.yml --extra-vars path2={}".format(l))

print("""<button class="open-button" onclick="openForm7()" style="position:absolute;top:61%;left:40%;height:7%">Click a Pic</button>

<div class="form-popup" id="myForm7">
  <form action="" class="form-container">
    <h1>Photo Session</h1>

    <button type="submit" class="btn">Click a Pic</button>
    <button type="button" class="btn cancel" onclick="closeForm7()">Cancel</button>
  </form>
</div>

<script>
function openForm7() {
  document.getElementById("myForm7").style.display = "block";
}

function closeForm7() {
  document.getElementById("myForm7").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
x=sp.getstatusoutput("sudo ansible-playbook photo.yml")

print("""<button class="open-button" onclick="openForm8()" style="position:absolute;top:69%;left:40%;height:7%">Partition</button>

<div class="form-popup" id="myForm8">
  <form action="" class="form-container">
    <h1>Partition</h1>

    <label for="email"><b>Path</b></label>
    <input type="text" placeholder="Ex:/dev/sdb" name="path1" required>

    <label for="email"><b>Partition number</b></label>
    <input type="Number" placeholder="Enter Partition Number" name="part_num1" required>

    <br><br><label for="email"><b>Select state</b></label>
    <input type="radio" name="state" value="present" required>Present
    <input type="radio" name="state" value="absent" required>Absent

    <br><br><label for="email"><b>Size</b></label>
    <input type="text" placeholder="Ex:200MiB/2GiB" name="size" required>

    <br><br><button type="submit" class="btn">Create Partition</button>
    <button type="button" class="btn cancel" onclick="closeForm8()">Cancel</button>
  </form>
</div>

<script>
function openForm8() {
  document.getElementById("myForm8").style.display = "block";
}

function closeForm8() {
  document.getElementById("myForm8").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
m=mydata.getvalue('path1')
n=mydata.getvalue('part_num1')
o=mydata.getvalue('state')
p=mydata.getvalue('size')
x=sp.getstatusoutput("sudo ansible-playbook parted.yml --extra-vars path1={} --extra-vars part_num={} --extra-vars state2={} --extra-vars size2={}".format(m,n,o,p))

print("""<button class="open-button" onclick="openForm9()" style="position:absolute;top:77%;left:40%;height:7%">Yum Configure</button>

<div class="form-popup" id="myForm9">
  <form action="" class="form-container">
    <h1>Yum Configure</h1>
    <button type="submit" class="btn">For GUI</button>
    <button type="button" class="btn cancel" onclick="closeForm9()">Cancel</button>
  </form>
</div>

<script>
function openForm9() {
  document.getElementById("myForm9").style.display = "block";
}

function closeForm9() {
  document.getElementById("myForm9").style.display = "none";
}
</script>""")
x=sp.getstatusoutput("sudo ansible-playbook yum.yml")

print("""<button class="open-button" onclick="openForm10()" style="position:absolute;top:85%;left:40%;height:7%">Add a User</button>

<div class="form-popup" id="myForm10">
  <form action="" class="form-container">
    <h1>Add User</h1>

    <label for="email"><b>Name</b></label>
    <input type="text" placeholder="Enter User Name" name="user_name" required>

    <button type="submit" class="btn">User Add</button>
    <button type="button" class="btn cancel" onclick="closeForm10()">Cancel</button>
  </form>
</div>

<script>
function openForm10() {
  document.getElementById("myForm10").style.display = "block";
}

function closeForm10() {
  document.getElementById("myForm10").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
q=mydata.getvalue('user_name')
x=sp.getstatusoutput("sudo ansible-playbook user.yml --extra-vars user_name={}".format(q))

print("""<button class="open-button" onclick="openForm11()" style="position:absolute;top:93%;left:40%;height:7%">Add a Group</button>

<div class="form-popup" id="myForm11">
  <form action="" class="form-container">
    <h1>Add Group</h1>

    <label for="email"><b>Group Name</b></label>
    <input type="text" placeholder="Enter Name here" name="groupname" required>

    <button type="submit" class="btn">Add Group</button>
    <button type="button" class="btn cancel" onclick="closeForm11()">Cancel</button>
  </form>
</div>

<script>
function openForm11() {
  document.getElementById("myForm11").style.display = "block";
}

function closeForm11() {
  document.getElementById("myForm11").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
r=mydata.getvalue('groupname')
x=sp.getstatusoutput("sudo ansible-playbook group.yml --extra-vars groupname={}".format(r))

print("""<button class="open-button" onclick="openForm12()" style="position:absolute;top:101%;left:40%;height:7%">Configure Bucket</button>

<div class="form-popup" id="myForm12">
  <form action="" class="form-container" method='POST'>
    <h1>Configure Bucket</h1>

    <label for="email"><b>Bucket Name</b></label>
    <input type="text" placeholder="Enter Name" name="b_name" required>

    <label for="email"><b>Access Key</b></label>
    <input type="password" placeholder="Enter Access Key" name="a_key" required>

    <label for="email"><b>Secret Key</b></label>
    <input type="password" placeholder="Enter Secret Key" name="s_key" required>
    
    <label for="email"><b>File Name</b></label>
    <input type="text" placeholder="Enter File Name" name="f_name" required> 

    <br><br><label for="email"><b>Select Mode</b></label><br>
    <input type="radio" name="mode2" value="get" required>Download
    <input type="radio" name="mode2" value="put" required>Upload
    <input type="radio" name="mode2" value="delobj" required>Delete   

    <button type="submit" class="btn">Configure Bucket</button>
    <button type="button" class="btn cancel" onclick="closeForm12()">Cancel</button>
  </form>
</div>

<script>
function openForm12() {
  document.getElementById("myForm12").style.display = "block";
}

function closeForm12() {
  document.getElementById("myForm12").style.display = "none";
}
</script>""")
mydata=cgi.FieldStorage()
s=mydata.getvalue('b_name')
t=mydata.getvalue('a_key')
u=mydata.getvalue('s_key')
v=mydata.getvalue('f_name')
w=mydata.getvalue('mode2')
x=sp.getstatusoutput("sudo ansible-playbook s3_main.yml --extra-vars b_name={} --extra-vars s_key={} --extra-vars s_key={} --extra-vars f_name={} --extra-vars mode2={}".format(s,t,u,v,w))


cmd="sudo ansible-playbook caas.yml"
output=sp.getoutput(cmd)
print("""<iframe width='20%' name='diframe'></iframe>""")
print("""<button class="open-button" onclick="location.href = 'http://192.168.43.38:2222'" style="position:absolute;top:30%;left:0%;height:7%">Get Console</button>""")

print("""
<style type="text/css">
body {
background: #000000;
}
canvas {
display: block;
}
</style>
<body data-rsssl=1>
<canvas id="canvas"></div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){
window.onload = function(){
//canvas init
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
//canvas dimensions
var W = window.innerWidth;
var H = window.innerHeight;
canvas.width = W;
canvas.height = H;
//snowflake particles
var mp = 50; //max particles
var particles = [];
for(var i = 0; i < mp; i++)
{
particles.push({
x: Math.random()*W, //x-coordinate
y: Math.random()*H, //y-coordinate
r: Math.random()*4+1, //radius
d: Math.random()*mp //density
})
}
//Lets draw the flakes
function draw()
{
ctx.clearRect(0, 0, W, H);
ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
ctx.beginPath();
for(var i = 0; i < mp; i++)
{
var p = particles[i];
ctx.moveTo(p.x, p.y);
ctx.arc(p.x, p.y, p.r, 0, Math.PI*2, true);
}
ctx.fill();
update();
}
//Function to move the snowflakes
//angle will be an ongoing incremental flag. Sin and Cos functions will be applied to it to create vertical and horizontal movements of the flakes
var angle = 0;
function update()
{
angle += 0.01;
for(var i = 0; i < mp; i++)
{
var p = particles[i];
//Updating X and Y coordinates
//We will add 1 to the cos function to prevent negative values which will lead flakes to move upwards
//Every particle has its own density which can be used to make the downward movement different for each flake
//Lets make it more random by adding in the radius
p.y += Math.cos(angle+p.d) + 1 + p.r/2;
p.x += Math.sin(angle) * 2;
//Sending flakes back from the top when it exits
//Lets make it a bit more organic and let flakes enter from the left and right also.
if(p.x > W+5 || p.x < -5 || p.y > H)
{
if(i%3 > 0) //66.67% of the flakes
{
particles[i] = {x: Math.random()*W, y: -10, r: p.r, d: p.d};
}
else
{
//If the flake is exitting from the right
if(Math.sin(angle) > 0)
{
//Enter from the left
particles[i] = {x: -5, y: Math.random()*H, r: p.r, d: p.d};
}
else
{
//Enter from the right
particles[i] = {x: W+5, y: Math.random()*H, r: p.r, d: p.d};
}
}
}
}
}
//animation loop
setInterval(draw, 33);
}
})
</script>
""")

