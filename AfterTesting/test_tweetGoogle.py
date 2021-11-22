import tweetGoogle as tg
import Gcloud
import benchmark


def test_long():
	x='''asdfqwaoiefhjqwoeifhqoweijfo[eirhvdcvuh-8917450ij-08d7fdfghjnqpeoruhgqerg
qerghqerpogjnqeoruigq[eroknfp[193h45tr
fdvhjnp139u5htp1[o3ui4htrp19[34uht1934[tho[jhfno[qerhgo[qerihg[qoerhgqer
gqeorughbqelrjhg;qoerjkghq;eroigh[qoeirhgqo[erihg;lqerkjh['oierhjfq
ergouiqerhnoplufnqp;eorifhp;qerojknc[qoeirhf[qoerkfnqe
rfq;eoirnfp;qoerhjfn;qeorihfjn;qoeirfn;qoeirjfnm;qoeirhnfqeriofqe
g4567dfc4567fg456fg
4567er4567fg45674567fg4567fg4567fg4567er4567er4567er45678e678fghjh90o98583456o5j6vbc346df4567yfc
456fcvj-hp340-pcvm578rt 578t
 568rtg45678r45678r4568rty45678r45678r456rty45678r6789er4567rt4567er4rt 4567rt6789km4678906784tgh6789rgm46789r
 4567df4567rr2q4e9fuj23oph5f1p3o4fhn1po3;uhf1p3o4ufp1o34hf
 134fjn134iujf1p34inf1p3o4uf134opuf1p3ou4nrf1p3ou4r1[o34uhr1op23uhr514o3ih5r134iorh245
 gergqerwgqergrthk67k46k467k467k467k467k467k467k467k467k
 467k467k467k467k467k46k467k467k467k467k6k	qerghqerpogjnqeoruigq[eroknfp[193h45tr
fdvhjnp139u5htp1[o3ui4htrp19[34uht1934[tho[jhfno[qerhgo[qerihg[qoerhgqer
gqeorughbqelrjhg;qoerjkghq;eroigh[qoeirhgqo[erihg;lqerkjh['oierhjfq
ergouiqerhnoplufnqp;eorifhp;qerojknc[qoeirhf[qoerkfnqe
rfq;eoirnfp;qoerhjfn;qeorihfjn;qoeirfn;qoeirjfnm;qoeirhnfqeriofqe
rfquioerbfhnpqeruhjfbnp;qerfhbqrp;iofhqep;rofhpqouih13op4uihnf13
4t1245jkntl256kjtn24piotb245ihvbt3l456hgv3khjv73567
3567kj35b67lk345h67b2;56uj7;2k3j64b7;24kjb56;2k4j5b6;245jkb6g24o56
2456jhvb245lkj6b2;45jk6b;24jk56b34jkm,56b,3m4n5b6;1ijk6b;23kjb623;lk6hjb232362
35623kl5jb623kj;b6235klj6bk;j6b245klj6b24;5jkb62456
245624562456jk245b2klj5b6k;jrthbngp9rotyghbopwrsh[wo4thgio[6hj57io390o4567g4567df4567fg4567fg4567dfc4567fg456fg
4567er4567fg45674567fg4567fg4567fg4567er4567er4567er45678e678fghjh90o98583456o5j6vbc346df4567yfc
456fcvj-hp340-pcvm578rt 578t
 568rtg45678r45678r4568rty45678r45678r456rty45678r6789er4567rt4567er4rt 4567rt6789km4678906784tgh6789rgm46789r
 4567df4567rr2q4e9fuj23oph5f1p3o4fhn1po3;uhf1p3o4ufp1o34hf
 134fjn134iujf1p34inf1p3o4uf134opuf1p3ou4nrf1p3ou4r1[o34uhr1op23uhr514o3ih5r134iorh245
 gergqerwgqergrthk67k46k467k467k467k467k467k467k467k467k
 467k467k467k467k467k46k467k467k467k467k6k'''
	assert tg.main(x)
	
def test_NLP():
	'''feed more than 1 text into google NLP
	and see if google can handle it.'''
	
	x = '''2joijr028fckf0mmiwrh98y4n208f3
	sdfjoqiewjfi2j2fp34fu109u3fiojrdsjfhpqiuewhfqjwkfnpoeiuvt
	whui24j2oifjiurewpncepwiurhvepwurhq
	dslkfjkjwfowejfweofijewoifwjef
	'''
	y = '''fjoiewjfwieofjiwjvoesjfdv;oijwadkjhasdlkjfh
	askdjfhaskdjfhalskjdf'''
	z ='''aksjfakjdhfa;skdjf
	daflkjhaldskjhflkasjdjf'''
	IN = [x,y,z]
	assert Gcloud.anaSentiment(IN)
	
def test_score():
	'''test what will happend if google NLP did not produce a output'''
	x = None
	assert tg.score(x)
	
def test_perform_NLP(benchmark):
	'''test the speed of the google NLP with a really large text'''
	
	x = '''3hepihepfaoijdapijepqojfqph4fpo1ih24fadsjfalksdjhfkjhfdkasjf
	sakdjfhaksjdhfksjdhfhqjfnpqiu4fndsjfhahufpqoiuewhfpqiwenpiuwfeq
	fieuhfpqiwnfepiquwedpiwqjendpiquwepieajnipnfapiurfpaierug
	qerihreapufreqkcmpeqoiuhqpufqeihupiuhpiuhpiuhiuhiuhiuh
	uhg8yggygygjoijowiejowkdweikdwejdiewjeidwkx0wicj0tgrgrfw
	cerfrefe;rforek384j08r53jr93jfeijwoivwpfjowekfeoifkoekieorifjvmmvmvfv
	eerfreofroifoikoeirkfpirkfp23f2.rkfkf.erfk0rf0.erf0erf0e9.c0e9irf0re9if0e9rif0rife
	er 0ire0feoijfoerfjcofjoejorijfoeirjf3j49jr48394rj4938r3498jr4r3odcdcdcdcwcw
	eweewfrg53hg5ggf3ut45h093u50tu958j87h9khjuu9j
	uj9k9okijuhynjuikjnhbgv6rcr6vb7n8mjk,ol'''
	IN = x + x + x + x + x + x +x + x + x + x + x + x + x + x + x + x + x + x +x + x + x + x + x + x + x
	
	benchmark(Gcloud.anaSentiment(IN), 0.1)
	
	
