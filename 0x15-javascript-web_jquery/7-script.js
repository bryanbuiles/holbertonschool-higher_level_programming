const $ = window.$;
const $name = $('#character');
$.ajax('https://swapi-api.hbtn.io/api/people/5/?format=json', {
  type: 'GET',
  success: function (name) {
    $name.append(name.name);
  }
});
