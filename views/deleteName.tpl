<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8">
        <link rel="stylesheet" href="/css/default.css" type="text/css" media="screen" charset="utf-8" />
        <title>Name Management DELETE</title>
        <script src="http://code.jquery.com/jquery-1.11.2.js"></script>
        <script type="text/javascript">

            function deleteName() {


              var data = '{"name":"' + $('#Name').val() + '"}';
              $.ajax({
                  url: "http://localhost:8000/names",
                  type: "DELETE",
                  contentType: "application/json",
                  data: data,
                  dataType: "json",
                  success: function(data){
                      $('.response').empty();
                      $('.response').append($('#Name').val() + " has been deleted");
                  },
                  error: function(data){
                    $('.response').empty();
                    $('.response').append("This name is invalid or doesn't exist");
                  }
              });
            };

        </script>
    </head>

    <body class="body">
        <h1>DELETE Names</h1>


        <!-- Contiendra notre formulaire de login -->
      <div class="formulaire">
          <form method="POST" action="">
              <label for="label Name">Name:</label>
              <input name="name"  id="Name"    type="text"  />
              <input type="button" name="submit" id="LoginButton" onClick="deleteName();" value="Delete"/>
            </form>
      </div>
      <a href="/">Back</a>
      <div class="response">
      </div>
    </body>
</html>
