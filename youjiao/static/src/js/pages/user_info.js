import 'normalize_css';
import 'main_css';
import area from 'area_js';
import 'birthday_js';
import '../modules/add_slides_itemhover.js';

$(function () {
  console.log($)
  let area_init = function () {
    for (let s = 0; s < area.length; s++) {
      let state = area[s];
      let stateName = state.state;
      $('<option />').appendTo('#select-state')
        .text(stateName)
        .attr({'value': stateName, 's_index': s});
    }
  };

  let area_select = function () {
    $('#select-state').change(function () {
      $('#select-city').empty().append('<option>-城市-</option>');
      $('#select-area').empty().append('<option>-县区-</option>');
      let s_index = $('#select-state option:selected').attr('s_index');
      let cities = area[s_index].cities;
      for (let c = 0; c < cities.length; c++) {
        let city = cities[c];
        let cityName = city.city;
        $('<option />').appendTo('#select-city')
          .text(cityName)
          .attr({'value': cityName, 'c_index': c});
      }
    });

    $('#select-city').change(function () {
      $('#select-area').empty().append('<option>-县区-</option>');
      let s_index = $('#select-state option:selected').attr('s_index');
      let c_index = $('#select-city option:selected').attr('c_index');
      let areas = area[s_index].cities[c_index].areas;
      for (let a = 0; a < areas.length; a++) {
        let areaName = areas[a];
        $('<option />').appendTo('#select-area')
          .text(areaName)
          .attr({'value': areaName, 'a_index': a});
      }
    });
  };

  area_init();
  area_select();

  $('.userinfo-right-top').find('a').click(function () {
    $('.userinfo-right-top').find('.active').removeClass('active');
    $(this).addClass('active');
    let index = $(this).parent('li').index();
    $('.userinfo-content-tab').addClass('display-none');
    $('.userinfo-content-tab').eq(index).removeClass('display-none');
  });

  $('#birthday_picker').birthdaypicker({
    dateFormat: "bigEndian",
    defaultDate: $.trim($('.userinfo-input-dateshow').text())
  });

  $('#click-edit-userprofile').click(function () {
    $('#birthdate').attr('name', 'birthday');
    $('.userinfo-input-show').addClass('display-none');
    $('.userinfo-form-input').removeClass('display-none');
  });

  $('#click-cancel-userprofile').click(function () {
    $('.userinfo-input-show').removeClass('display-none');
    $('.userinfo-form-input').addClass('display-none');
  });


  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $('#avatar-img').attr('src', e.target.result);
        reader.readAsDataURL(input.files[0]);
      }
    }
  }
  console.log(readURL)
  $("#avatar-upload-input").change(function () {
    readURL(this);
  });
});
