function fetchDev(){
  var cep = $('#cep').val();
  let resp;
  let request = new XMLHttpRequest();
  request.open('GET', "http://localhost:8000/api/user/zipcode/" + cep, true);

  
  request.onload = function() {
    if (request.readyState == 4 && (request.status >= 200 && request.status < 400)) {
        // Success!
        resp = request.responseText;
        
        let obj = JSON.parse(resp);
        console.log(resp);
        console.log(obj);
        
        var dataSet = [];
        $.each(obj, function(index,data){
          dataSet.push([data.id,data.name,data.username,data.zipcode]);
        });
        $('#tabledevs').DataTable({
          paging: false,
          searching: false,
          destroy: true,
          retrieve: false,
          data: dataSet,
          columns: [
            { title: 'Id' },
            { title: 'Nome' },
            { title: 'GitHub' },
            { title: 'CEP' }
          ]
        });
        

    } else {

    }
  };
  request.onerror = function() {
      //There was a connection error of some sort
      console.log("Erro:"+request);
  };
  request.send();
}

$("#formFetchDev").on("submit", function (event) {
  event.preventDefault();

  fetchDev();
});

function createDev(){
  var data = newFunction();
  console.log(data);

  function newFunction() {
    var name = $('#name').val();
    var username = $('#username').val();
    var zipcode = $('#zipcode').val();
    var data = '{"name":"' + name + '","username":"' + username + '","zipcode":"' + zipcode + '"}';
    return data;
  }

  let resp;
  let request = new XMLHttpRequest();
  request.open('POST', "http://localhost:8000/api/users/", true);

  request.onload = function() {
    if (request.readyState == 4 && (request.status >= 200 && request.status < 400)) {
        // Success!
        resp = request.responseText;

        //console.log(resp);
        //document.getElementById().innerText=resp;

    } else {

    }
  };
  request.onerror = function() {
      //There was a connection error of some sort
      console.log("Erro:"+request);
  };
  request.send(data);
}

$("#formCreateDev").on("submit", function (event) {
  event.preventDefault();

  createDev();
  alert("Desenvolvedor cadastrado!");
  window.location.href = "index.html";
});