#!/usr/bin/python3
def fact(e, s = 1):
    r = 1
    for i in range(s, e+1):
        r = r * i
    return r
 
def bin(n, r):
    return 1 if r == 0 else fact(n, max(n-r, r)+1)/fact(min(r, n-r)) 

def height1(e, d):
    return(sum([bin(d, i) for i in range(1, min(d, e)+1)]))

#pascal = [[1], [1,1], [1,2,1]]
#for i in range(3, 1000):
#    pascal.append([1] + [ pascal[i-1][j] + pascal[i-1][j+1] for j  in range(len(pascal[i-1])/2+1)])
#    print(pascal[i])

def bin_sum1(n, e):
    u, l, g = 1, 1, 0
    for i in range(1, e+1):
        l = l * i
        u = u * (n-i+1)
        g += u/l
    return g

def bin_sum(n, e):
    print('calling:', n, e)
    m = 1
    s = 0
    print m,
    for i in range(min(n-e-1, e)):
        m = (m *(n-i))/(i+1)
        print m,
        s += m

    if min(n-e-1, e) != e:
        s = 2**n - 2 - s + (1 if e > n else 0)
    return s


        
def height(e, d, func):
    entries = min(e, d)  
    s = 0
    #if entries > d/2:
    #    s = 2**d - 2 - func(d, d-entries-1) + (1 if e > d else 0)
    #else:
    s = func(d, entries)
    return s

#n = 2000
#for i in range(2000):
#    print(n, i, bin(n, i))

print(bin_sum(19, 16)%998244353)
print(bin_sum(10, 7))
r = 2**19-2-bin_sum(19, min(16, 19-16-1))
print(r % 998244353)

#print(bin_sum(20000, 20000) == 2**20000)
#print(height(100, 200, bin_sum1))
#print(height(100, 200, bin_sum))
import sys
sys.exit(0)
print(height(10000, 20000))
n = 15
e = 2
for i in range(1, n):
    print(height(i, n), height1(i, n))
#print(height(15834, 15383) - 55516656020216783447066546102017042803986430214071707721924543019659918829983909609085582481898374714657505353734675923849987642724549658928760983757383293935859230279946790206970908364330165015535730704409830184339663031546192459527270461008682904255536791160577391558441538360792250784217362385971799734810399950984518312332800175350704387614533631651651119252475952714465061639617698862372371066187460420440827061443668400734719180225886533538624130586275560423784683744527895020494962066698856234542181651972346261048074709572612738611738816796990593216745512895574674935499371200888014968242587316889523112713129090093050070072142100186681951711902124239124153172301595233316628029134600310075236506222326493121380190600791836536745763821552081035932005079747318847743490142303980004722020361494664240046081443237122541342546952186599390547514906446330641546450184448402495701169329449668269240398140612329727136640113172639535255515896897073977235583013991887197277402826530215110951471983467553535558785952610005285733589943306332910206199466037373201485337964756169479058735773459538850787891150642167289726566178474918142240390846646035826868628581162717238834501363137931792117512564958822153168450737928316410959777529923866209095532982536827200852441364767423354052456647676474952296298699360445243814872301983379388271307387101251984987620206618061115760484387279849907349085888132057299304543674133596384852583512509817578574690977148531188088100999702184885203875976428981901920211864177994360842386728815037404954736305168311636597742355392277837129885376706813134939695526233544013129651092569784935067731203822106646865241075930676389078058008989867786973915063089904710446180918846134657520165622578512569516423384129264434892067571595069026893279143989433831654716501163596876717056841523501789719505351484596088012650975676100947435593160078443180701742862965547667825503329817273722740151381077145212470676564021947285050908288159571401589861305114306920225735104447394912842778790802247138372723631838651841605080173890181955822877483360178506110434434355172494348570363511776222521827182593728090639999547874116540432080010499366732547625029801725411793308606445144060036207756035193014020348167821477530554507939034742297166786627373378530013105035200956603924828928529840590840659358541829899823033732021241906340408928246022470523136772464802113665572703646424883540354269147918380717666674953896614495412664603194797563651752308307538451419320556460401693502279629584763932185452141568448188594234912140505557234291413419312880566290226996311229031070514799360999754364387232513856502181350781304341583652207572418741632912071842495255912447198039720801067473526656159980319157637324419982522858032912489424918789726942459252976473997773102392708624367753226907729644117949999080887893043681519188888745319421121366532311786844491437057487772219746129599153905818074806219902758884866762867122741404128459059218983019133646098290902598667172477685439043730048295486426782362072611017789780372086309145135673431145135368645040729748542912348230204120087204615150963085485530215161846263494147879604398323229743366091919599779649091098953881412539050200117534712061081410512490132133830377170715744927983221266434356294283567403714754110003546668957396055009392085271607657584400846719412160139708544771207147676206052703298557982898258407069515625780942923266071374242179644014161360356132120469503273890650182295701038416839802164637048858208445124768585826573652535942067078019606637793077998901674167504914346578527738296234560088462978749897962208273609179626236571223262216867582643564226125632310632435716593018543044888670840515987091208730527912906768877593608014126867209519880076892170021127702666887951323576808201739854477659546963065201101378271486965616103904737934174513335273586304024405368653768261940051303862189086377088740639013836219384642187702555999198433804837233981523313827565933128847012184724830353236236578175036938839969145884444734987690899078791335764598322415722046719162965350711889605867053298877416498554673155651385519756594159803176823687871749723649032272326963327521857220860661352048818854410215324265268661448555734023859871471950964985656027954017555676314576092567637188002339733988766659689279109724743515437308742923225048485760596255798315723972183170132295287907539885446175683395765134326480416252332294632911099742070362141516669292047663658096735345249112563288820812432059293177367459853660332591128417730903763843185928990761768466746096797180864925696957026070712405924279821779066964083069125219876791967729420111209456738063206907697525612670353407L)
print(height(9477,10000))
    
