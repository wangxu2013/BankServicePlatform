//注册
var Customer =  Backbone.Model.extend({
    url: '/api/customer',
    //解析异步请求返回的结果，fetch方法与save方法都会调用它
    parse: function(res) {
        //保存customeId和token
        sessionStorage.setItem(key_customer_id, res.data.customer.id);
        sessionStorage.setItem(key_token, res.data.token);
        //localStorage.setItem(key_customer_id, 1);
        //localStorage.setItem(key_token, "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUwMjc5MjM4NCwiaWF0IjoxNTAyNzA1OTg0fQ.eyJpZCI6NjZ9.r2Uxsm_5YDKdMNrlUof4bYr01qL-w6T_He4NdJnq6jg");

        changePage('wdzh');

    }
});

var customer = new Customer;
$("#subBtn").click(function() {
    var timestamp = new Date().getTime();
    customer.url = customer.url + "?t=" + timestamp;
    var obj = [];
    obj["customer"] = $('#contentForm').serializeJSON();
    customer.save(obj, {
        beforeSend: sendAuthentication
    });
});