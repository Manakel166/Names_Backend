<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8">
        <link rel="stylesheet" type="text/css" media="screen" charset="utf-8" />
        <title>Name Management Delete</title>
        <script src="http://code.jquery.com/jquery-1.11.2.js"></script>
        <script type="text/javascript">
            function printName(data){
              var i = 0;
              $('.response').append("<ul>");
              while(data.names[i] != null){
                $('.response').append("<li>" + data.names[i]);
                $('.response').append("</li>");
                i++;
              }
              if(i==0){
                $('.response').append("No name in database");
              }
              $('.response').append("</ul>");
            };
            window.onload = function onLoad(){
              $.ajax({
                  url: "http://localhost:8000/names",
                  type: "GET",
                  contentType: "application/json",
                  dataType: "json",
                  success: function(data){
                    printName(data);
                  },
                  error: function(data){
                    alert(data);
                  }
              });

            };


        </script>
    </head>

    <body>
        <h1>List Name</h1>


        <p class="response"></p>

        <a href="/">Back</a>

    </body>
</html>
