//  function constructor
var Person = function (firstName, lastName) {
    this.firstName = firstName
    this.lastName = lastName
  }
  
  //  function constructor 的 prototype
  Person.prototype.getFullName = function () {
    return this.firstName + ' ' + this.lastName
  }
  
  //  根據 function constructor 所建立的物件 Customer1
  var Customer1 = new Person('John', 'Doe')
  
  //  透過for...in輸出
  for (var prop in Customer1) {
    console.log(prop + ': ' + Customer1[prop])
  }