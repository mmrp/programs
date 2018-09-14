function integerSquareRoot(n) {
  // Splits `n` into pairs, but first group is only one digit if length of `n` is odd
  let N = n.length%2 ? [n[0]].concat(n.slice(1).match(/.{2}/g)||[]) : n.match(/.{2}/g), S = '', remain = ''
  
  while (N.length) {                                    // This is based on the square root algorithm
    remain += N.shift()                                 // that is similar to long division.
    let start = S ? multiply(S,2) : '', chunk, m=10     // `m` is the digit being determined in each round.
    do chunk = multiply(start + --m, m)                 // It is decremented before each use, so it
    while (!LTE(chunk, remain))                         // always ends up being 0-9.
    S += ''+m
    remain = subtract(remain, chunk)
  }
  return S
}

// Helpers borrowed from my other kata solutions

const LTE = (x,y) => x==y || x.length < y.length || (x.length==y.length && [...x].map((d,i)=>d-y[i]).find(s=>s!=0) < 0)

const multiply = (a,b,c=0) => [...a].reverse()
  .map((d,i,m) => (v = d*b+c , i == m.length-1 ? v : ( c = ~~(v/10) , v%10 ) ) )
  .reverse().join``.replace(/^0+/,'') || '0'

const subtract = (a,b) => 
  [a,b].map(n=>[...n].reverse()).reduce((a,b) =>
    a.reduce((r,d,i) => {
      let s = d-(b[i]||0)
      if (s<0) {
        s+=10
        a[i+1]--
      }
      return ''+s+r
    },'').replace(/^0+/,'')
  )

  function divideStrings(a,b) {
  if(!strvalcmp(a, b)) return ['0',a];
  var quo = '', len = a.length-b.length, rem = a.slice(0,b.length);
  a = a.slice(b.length);
  for(let i=0; i<=len; i++) {
    var dgt = 0;
    for(;strvalcmp(rem,b);dgt++) rem = subtractStrings(rem,b);
    quo=(quo==='0'?'':quo)+dgt;
    rem=(rem==='0'?'':rem)+(a[0]||'');
    a=a&&a.slice(1);
  }
  return [quo+a,rem||'0'];
}
var strvalcmp=(a,b)=>a.length>b.length || (a.length===b.length && a>=b);
function subtractStrings(a, b) {
  if(a===b)return '0';
  var res = '', c = 0;
  a = a.split(''); b = b.split('');
  while (a.length || b.length || c) {
    c += ~~a.pop() - ~~b.pop();
    res = (c+10) % 10 + res;
    c = -(c < 0);
  }
  return res.replace(/^0+/, '');
}
