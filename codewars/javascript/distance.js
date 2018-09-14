// complete the function to calculate the distance between two coordinates.
// Input: the two coordinates
// Output: return the distance in kilometers
function distance(coord1, coord2) {
    function get_degrees(inp) {
        var flds = inp.split(/[^\d\w]+/)
        var lat = flds[0] * 1 + flds[1]/60 + flds[2]/(60*60)
        var lon = flds[4] * 1 + flds[5]/60 + flds[6]/(60*60)
        console.log(flds)
        if (flds[3] == 'S')
            lat = -lat

        if (flds[7] == 'W')
            lon = -lon
      return [lat * Math.PI/180, lon * Math.PI/180]
    }   
          
    dg = get_degrees(coord1)
    lat1 = dg[0]
    lon1 = dg[1]
    dg = get_degrees(coord2)
    lat2 = dg[0]
    lon2 = dg[1]

    var dlon = lon2 - lon1; 
    var dlat = lat2 - lat1;
    var a = Math.pow(Math.sin(dlat/2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(dlon/2), 2)  
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)) 
    var R = 6371
    var d = R * c 
    console.log(d)
    //console.log(coord1, get_degrees(coord1));
    console.log(coord2, get_degrees(coord2));
    d = parseInt(d)
    d = d - d % 10
    return(d)

}

