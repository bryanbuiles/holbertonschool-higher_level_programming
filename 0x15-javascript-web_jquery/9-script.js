const $ = window.$;
$.ajax('https://fourtonfish.com/hellosalut/?lang=fr', {
  type: 'GET',
  dataType: 'json'
}).done(function (data) {
  $('DIV#hello').append(data.hello);
});
