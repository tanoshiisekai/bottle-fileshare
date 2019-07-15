<html>
  <head>
    <title>文件分享</title>
    <style type="text/css">
     .filename
     {
       float: left;
       text-decoration: none;
       color: #4B67B3;
       font-weight: bold;
     }
     .deletebutton
     {
       float: right;
       margin-right: 50%;
       text-decoration: none;
       color: #2C2952;
       font-weight: bold;
     }
    </style>
  </head>
  <body>
    <h1>已上传的文件</h1>
    <ul>
      %for file in filelist:
      <li><a href="{{file[0]}}" class="filename"> {{file[1]}} </a><a href="/deletefile?fileurl={{file[0]}}" class="deletebutton">删除</a></li>
      %end
    </ul>
    <hr/>
    <h1>上传文件</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
      请选择一个文件：<input type="file" name="upload"/><br/>
      <input type="submit" value="开始上传"/>
    </form>
  </body>
</html>
