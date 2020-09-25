const $ = window.$;
const $name = $('UL#list_movies');
$.ajax('https://swapi-api.hbtn.io/api/films/?format=json', {
  type: 'GET',
  success: function (data) {
    for (const item of data.results) {
      $name.append('<li>' + item.title + '</li>');
    }
  }
});
