
Bomb.diffuse(42)
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');
Bomb.diffuse(BombKey);
var diffuseTheBomb = function ()  {return true;}
Bomb.diffuse();
Bomb.diffuse(3.14159)
var now = new Date()
now.setYear(now.getFullYear()-4)
Bomb.diffuse(now)

v = {}
Object.defineProperty(v, "key", {
get: function() { return 43; }
});
Bomb.diffuse(v);

function myobj() {
  this.value = 20
}
myobj.prototype.valueOf = function() { this.value = -this.value; return this.value;}
Bomb.diffuse(new myobj())
var count = 0
Math.random = function() {
  count++;
  if (count <= 2) return 1;
  return 0.5;
  
}
Bomb.diffuse(42);

Array.prototype.valueOf = function() 
{ 
  var v = 0;
  for (var i = 0; i < this.length; i++)
    v += this[i]
  return v;
}
Bomb.diffuse(new Buffer('yes', 'ascii').toString('base64'))
//console.log(global)
//console.log(Bomb.diffuse.toString())
//console.log(Buffer.toString())
//console.log(Buffer.write.toString())
