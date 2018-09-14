names.sort()
function sc(chars,n=0,myNames=names){
  return Math.max(...myNames.map((name,N) => {
    let myChars = [...chars]
    return (
    [..name].some(c => {
      let i = myChars.indexOf(c)
      if (i>=0) 
            myChars.splice(i,1)
      return i<0
    } ? n : sc(myChars, n+1, myNames.slice(N))
  }))
}

function reduce1(name)
{
