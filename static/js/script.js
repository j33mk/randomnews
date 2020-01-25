(function() {
    $('#btnReload').click(function () {
          $('#quoteContainer').hide();
          $('#txtPoweredBy').hide();
          $("#txtPoweredBy").animate({left:200, opacity:"show"}, 1500);
          $.ajax({
              url: "http://127.0.0.1:5000/fortune",
              success: function (result, status, xhr) {
                  if (result.status === 'awesome') {
                      $("#txtQuote").text(result.data);
                      $('#quoteContainer').fadeIn('slow');
                  }

              }
          });
      });
      initNews();
      $('#btnNewsReload').click(function () {
        $('#newsContainer').hide();
        $('#txtPoweredBy').hide();
        $("#txtPoweredBy").animate({left:200, opacity:"show"}, 1500);
        $.ajax({
            url: "http://127.0.0.1:5000/randomnews",
            success: function (result, status, xhr) {
                if (result.status === 'awesome') {
                    console.log(result.data[1]);
                    $("#txtNews").text(result.data[0]);
                    $('#newsLink').text(result.data[1]);
                    $("a").attr("href", result.data[1])
                    $('#newsContainer').fadeIn('slow');
                }

            }
        });
      });
}).call(this);
function initNews(){
    $('#newsContainer').hide();
        $('#txtPoweredBy').hide();
        $("#txtPoweredBy").animate({left:200, opacity:"show"}, 1500);
        $.ajax({
            url: "http://127.0.0.1:5000/randomnews",
            success: function (result, status, xhr) {
                if (result.status === 'awesome') {
                    console.log(result.data[1]);
                    $("#txtNews").text(result.data[0]);
                    $('#newsLink').text(result.data[1]);
                    $("a").attr("href", result.data[1])
                    $('#newsContainer').fadeIn('slow');
                }

            }
        });
}