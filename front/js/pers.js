function fetchDev() {
  var cep = $("#cep").val();
  let resp;
  let request = new XMLHttpRequest();
  // request.open("GET", "http://localhost:8000/api/user/zipcode/" + cep, true);
  request.open("GET", "http://localhost:8000/api/users/", true);
  // http://localhost:8000/api/users/

  request.onload = function () {
    if (
      request.readyState == 4 &&
      request.status >= 200 &&
      request.status < 400
    ) {
      // Success!
      resp = request.responseText;

      resp = "[" + resp + "]";
      
      let obj = JSON.parse(resp);
      // console.log(resp);
      console.log("obj", obj);

      var dataSet = [];
      $.each(obj[0], function (index, data) {
        console.log("data", data);
        dataSet.push([data.id, data.name, data.username, data.zipcode]);
      });
      console.log("dataSet", dataSet);

      $("#tabledevs").DataTable({
        paging: false,
        searching: false,
        destroy: true,
        retrieve: false,
        data: dataSet,
        columns: [
          { title: "Id" },
          { title: "Nome" },
          { title: "GitHub" },
          { title: "CEP" },
        ],
      });

    } else {
    }
  };
  request.onerror = function () {
    //There was a connection error of some sort
    // console.log("Erro:" + request);
  };
  request.send();
}

$("#formFetchDev").on("submit", function (event) {
  event.preventDefault();

  fetchDev();
});

function createDev() {
  var data = newFunction();
  console.log(data);

  function newFunction() {
    var name = $("#name").val();
    var username = $("#username").val();
    var zipcode = $("#zipcode").val();

    var data =
      '{"name":"' +
      name +
      '","username":"' +
      username +
      '","zipcode":"' +
      zipcode +
      '"}';
    return data;
  }

  let resp;
  let request = new XMLHttpRequest();
  request.open("POST", "http://localhost:8000/api/users/", true);

  request.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  request.setRequestHeader("Content-Type", "application/json");
  request.setRequestHeader("Access-Control-Allow-Origin", "*");
  request.setRequestHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, OPTIONS, PUT, PATCH, DELETE"
  );
  request.setRequestHeader(
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
  );
  request.setRequestHeader("Access-Control-Allow-Origin", "*");
  request.setRequestHeader(
    "Access-Control-Allow-Headers",
    "Origin, X-Request-Width, Content-Type, Accept"
  );
  request.setRequestHeader("Access-Control-Allow-Headers", "Access-Control-Allow-Origin");

  request.onload = function () {
    if (
      request.readyState == 4 &&
      request.status >= 200 &&
      request.status < 400
    ) {
      // Success!
      resp = request.responseText;

      console.log(resp);
      document.getElementById().innerText = resp;
    } else {
    }
  };
  request.onerror = function () {
    //There was a connection error of some sort
    console.log("Erro:" + request);
  };

  request.send(data);
  // request.send(JSON.stringify(data));
}

$("#formCreateDev").on("submit", function (event) {
  event.preventDefault();

  createDev();
  // alert("Desenvolvedor cadastrado!");
  // window.location.href = "index.html";
});
