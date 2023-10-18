import ee
ee.Initialize()
aos = ee.Geometry.Polygon([[2.406308031112067,36.595170778587892],[2.406525162881822,36.596042414115516],[2.4064865,36.5965177],[2.406360177603492,36.596659698433186],[2.406464931123776,36.59688478676587],[2.406423289414509,36.596915830798395],[2.406366775666216,36.596927770807582],[2.406283492247681,36.596832250682375],[2.406247799354023,36.596748670475804],[2.405815766620348,36.597102691730086],[2.406693960524751,36.597942664834889],[2.406268620208658,36.598148030002307],[2.4063792,36.5983611],[2.406450059084754,36.598370110323977],[2.406536316911094,36.598439361046232],[2.406542265726704,36.598513387611618],[2.406741783422591,36.598650356993332],[2.407890416064237,36.599047093166376],[2.408167224333973,36.599320491722899],[2.408125488451433,36.59945709539587],[2.40821538112152,36.599531840699441],[2.40830848424411,36.599616895611994],[2.408186487048992,36.599781850326629],[2.409315343303238,36.601057709127446],[2.409123308099345,36.601357386710497],[2.408873457843738,36.602054640007992],[2.408445143119841,36.602107172535391],[2.407874056821312,36.601944799153294],[2.4077734,36.6020537],[2.4076688,36.6021527],[2.4075401,36.6022475],[2.4073389,36.6022862],[2.4070063,36.6024133],[2.4066925,36.6025748],[2.406443211339802,36.603057674809683],[2.40656520853492,36.603356641635571],[2.406770677495119,36.603470042542284],[2.406969725550312,36.603825707941063],[2.406626,36.6044247],[2.406552366724906,36.604892694298073],[2.406412766724907,36.605105594298067],[2.406275366724906,36.605464694298071],[2.406240254804135,36.605506371794917],[2.406143654804135,36.605902571794921],[2.405948801654322,36.606176151085791],[2.405745288079228,36.60642497749685],[2.4057607,36.6066036],[2.405820228232069,36.606642743820309],[2.4057992,36.6072383],[2.4057488,36.6075011],[2.405774124911093,36.607780474927829],[2.405720585570607,36.607883144485569],[2.405595660442804,36.607811514576014],[2.405330938148173,36.607907021107302],[2.404910059443788,36.608287852224763],[2.404697389285742,36.608513484821039],[2.404694414877937,36.608666293823497],[2.4051132,36.6089635],[2.4048021,36.6092133],[2.4046197,36.6094458],[2.4044266,36.6098678],[2.4040189,36.6112199],[2.4039277,36.6117797],[2.403875,36.6122578],[2.4040035,36.6131147],[2.4039974,36.613403],[2.403822913391116,36.613768508082252],[2.4041422,36.6141523],[2.4042764,36.6149919],[2.4044802,36.6154225],[2.404548668895496,36.615711892583249],[2.404447539030132,36.615974508353688],[2.4044641,36.616219],[2.4045499,36.6165893],[2.4045929,36.6169553],[2.40486990493842,36.617067935309827],[2.405179243350124,36.617130007117325],[2.405425025806916,36.617293167152816],[2.405533197878901,36.617390230689459],[2.405644347737484,36.617469634453748],[2.405836435816711,36.617713417035745],[2.406032273419401,36.618012327051453],[2.4067654,36.6191684],[2.407409557543235,36.620189696939164],[2.407512292023335,36.62056074555651],[2.407615026503434,36.620962712876633],[2.40764071012346,36.621127621940104],[2.407576501073397,36.621534739680072],[2.407396715733223,36.621874861713103],[2.407287560348117,36.622039768825303],[2.407293981253123,36.622225288904851],[2.407375784058005,36.622393122181052],[2.40753797564336,36.622730313526034],[2.407615026503435,36.623142576069995],[2.407627868313448,36.623364166276318],[2.407595763788416,36.623647594681529],[2.4074253,36.6238011],[2.4071302,36.6238829],[2.406574839892426,36.623727469771133],[2.406099692921965,36.623789308493343],[2.405669492286548,36.624088194951284],[2.405226449841118,36.624335548384856],[2.404622884770534,36.624603513708834],[2.404378890380297,36.624778721301588],[2.403685432639625,36.625428016554963],[2.403646907209588,36.625737202848441],[2.403865217979799,36.626067000194439],[2.403364387389313,36.626551387487943],[2.402516827928492,36.626819345108473],[2.402041680958031,36.627066689777472],[2.401463799507471,36.627303727673741],[2.401078545207098,36.627489235084035],[2.400808867196836,36.627623212380456],[2.400641923666674,36.62772627168075],[2.400603398236637,36.627932389867922],[2.4004086,36.6281881],[2.4006791,36.6287648],[2.4009685,36.6293507],[2.4012193,36.6300748],[2.4011909,36.6306306],[2.4010192,36.6311418],[2.4007994,36.6314837],[2.4002116,36.6317705],[2.3992857,36.632158],[2.3978743,36.6327226],[2.3971507,36.6329223],[2.3963962,36.6330142],[2.393978629496468,36.633502525122537],[2.393131070035647,36.633626186831542],[2.393079702795597,36.633203675173114],[2.393041177365559,36.632523529588291],[2.39264950216018,36.632472003162988],[2.3924049,36.632493],[2.3920508,36.6327255],[2.3912676,36.632803],[2.3907699,36.6335236],[2.3902913,36.6345938],[2.3894437,36.6348004],[2.3893794,36.6346971],[2.3889931,36.6347918],[2.3888322,36.6347229],[2.388564,36.6348262],[2.3885854,36.6349984],[2.3876842,36.6353342],[2.3879095,36.6350328],[2.387037631184739,36.634986452532168],[2.386472591544191,36.634955537669285],[2.386270333036494,36.635009638671178],[2.386212544891439,36.635128145494981],[2.386087337243818,36.635159060288593],[2.386071284981301,36.635262109511082],[2.385952498238686,36.635522308184512],[2.385824080138562,36.635653695299595],[2.3857959,36.6359626],[2.3858462,36.6363991],[2.3855833,36.6363819],[2.3853849,36.6364077],[2.3852594,36.6364969],[2.3851522,36.6368494],[2.385399,36.6371335],[2.3851737,36.6373659],[2.3848196,36.6372368],[2.3845686,36.6369846],[2.3829313,36.6364448],[2.3823688,36.6363201],[2.3810595,36.6366083],[2.3809787,36.6369097],[2.3812362,36.6374606],[2.3812255,36.6377706],[2.3810071,36.637797],[2.3806783,36.6376673],[2.380292,36.6374865],[2.3795706,36.6370646],[2.3790904,36.6356871],[2.3788437,36.6357474],[2.3786183,36.635403],[2.3781248,36.635515],[2.378039,36.635403],[2.3769339,36.6357818],[2.3766335,36.6360487],[2.3764404,36.636066],[2.3763653,36.6362295],[2.3765906,36.6369269],[2.3767193,36.6369958],[2.377288,36.6366342],[2.3775776,36.6365739],[2.3776849,36.6369871],[2.377127,36.6377017],[2.3763331,36.638554],[2.376376,36.6390791],[2.3765799,36.6392599],[2.3766442,36.639501],[2.3763975,36.63994],[2.3761395,36.6400446],[2.37614,36.6397506],[2.3760863,36.6394924],[2.3759732,36.6391708],[2.3759625,36.6388651],[2.3758176,36.6386499],[2.3758718,36.6384765],[2.3760005,36.6383646],[2.3759254,36.6382096],[2.3759254,36.6377878],[2.3756679,36.6371852],[2.3752388,36.6373057],[2.3740693,36.6377017],[2.3731359,36.6379255],[2.373046479176177,36.638119094323343],[2.372930902886065,36.63825305313901],[2.37261627854076,36.638438534191557],[2.372308075100461,36.638484904384924],[2.372025555280187,36.63835609822334],[2.371659563694832,36.6382066828061],[2.371267888489452,36.638067571639908],[2.37081200423401,36.638144855652136],[2.370381803598594,36.638330336965183],[2.370105704683326,36.63791300338287],[2.36950213961274,36.637454449062353],[2.368262904946539,36.637155614440772],[2.3676394,36.6372874],[2.3666309,36.6382172],[2.366362317064696,36.638412772960969],[2.366670520504996,36.638739939949531],[2.366721887745046,36.639247432450382],[2.366490735164822,36.639510193751448],[2.366253161679592,36.639649302312719],[2.365970641859318,36.639762649843576],[2.365733068374088,36.640025409387341],[2.365379918598745,36.640504556836355],[2.364968980678347,36.640581838403868],[2.364391099227787,36.640602446808771],[2.363749008727165,36.640494252621501],[2.363209652706642,36.640355145586007],[2.362233675145696,36.640525165261948],[2.361687898220167,36.640757009669869],[2.360975177764475,36.640308776518339],[2.360679816134189,36.640009952968398],[2.360480768078991,36.639700823938313],[2.36031382454883,36.639608084987401],[2.360069830158593,36.639577171978971],[2.359890044818418,36.639376237121695],[2.359737928234919,36.639351615544143],[2.359402056037945,36.63901558349928],[2.359132378027684,36.638696146023733],[2.358824174587384,36.638353522097916],[2.358576969744644,36.638397316218473],[2.358589811554657,36.638551883503844],[2.358355448521929,36.638644623726208],[2.358275187209351,36.638417925207776],[2.358185294539264,36.63842565357735],[2.358056876439139,36.638497784989234],[2.358040824176624,36.638830103836014],[2.357828934311418,36.638812071067164],[2.357414785938518,36.638971789730185],[2.357642728066239,36.639350476204669],[2.357893143361482,36.639306682625936],[2.357934879244022,36.639556563299777],[2.357950931506538,36.63985538860841],[2.35771656847381,36.639967447800316],[2.35753999358614,36.640209598141048],[2.357613833993712,36.640529029341117],[2.357475784536077,36.640688744444446],[2.357267105123375,36.640696472586214],[2.357129055665741,36.640606310884081],[2.357023110733139,36.640302336367839],[2.356881850823001,36.640292032125934],[2.356920376253039,36.640469780105683],[2.356181972177322,36.640554789864048],[2.355989345027136,36.640080794863074],[2.355661878871818,36.639802579047682],[2.355128943756302,36.639864404871268],[2.354788635790972,36.639823187661058],[2.354827161221009,36.6394213187058],[2.354377697870574,36.63934918815859],[2.354120861670325,36.63921007905541],[2.353742028274957,36.639333731603983],[2.35347,36.6396387],[2.3527726,36.6398625],[2.3522361,36.6400778],[2.351541076407264,36.640353818138259],[2.350961776407264,36.640379618138255],[2.350769149257077,36.640662983966322],[2.350550838486866,36.640853611300578],[2.35044168310176,36.641033934020435],[2.350502681699318,36.64113955141746],[2.350621468441933,36.641193648076943],[2.350836568759642,36.641149855546018],[2.350913619619716,36.641422914450189],[2.350704940207014,36.641556867521004],[2.350361421789181,36.641634148032828],[2.349934431606267,36.641407458311647],[2.349667964048509,36.641337905649813],[2.34935976060821,36.641198800137772],[2.349179975268036,36.641005597620982],[2.349109345312967,36.640930892517908],[2.349157502100514,36.640706776774039],[2.34916231777927,36.640500692755971],[2.349005005606617,36.640471068133053],[2.348899060674014,36.640401514625765],[2.348857324791474,36.640283015913163],[2.34866790809379,36.640241798926915],[2.348531463862408,36.640170957180295],[2.348290679924674,36.639998360652172],[2.348486517527364,36.639722720618799],[2.348608514722482,36.639519210054722],[2.348539489993665,36.639371084939022],[2.348106078905746,36.639293802156899],[2.347810717275459,36.63939684584917],[2.347348412115011,36.639309258719521],[2.347008104149681,36.639190758326791],[2.346488010844177,36.639077409954481],[2.34624401645394,36.639252584641383],[2.345730344053442,36.639340171835471],[2.345261617987988,36.639371084939008],[2.344864111819921,36.639091816854972],[2.344569111819921,36.639001516854968],[2.344279219522036,36.638894506547508],[2.344073750561837,36.638739939949552],[2.343990278796756,36.638642047610453],[2.343823335266594,36.638889354332569],[2.343566499066346,36.638997550773865],[2.34316840295596,36.638791462183335],[2.342860199515662,36.638956333099856],[2.342423577975238,36.639141812459208],[2.342096111819921,36.639152116854966],[2.34138339136423,36.639641574065919],[2.341075187923931,36.639894029727508],[2.340696354528564,36.640012529038451],[2.34022762846311,36.640234070739538],[2.339450698957357,36.639976464050065],[2.338937026556858,36.639924942608808],[2.338484738675016,36.6395860327478],[2.337959038675017,36.639525732747799],[2.337680138675017,36.639241632747805],[2.336830969714817,36.6393994219397],[2.335906359393921,36.6393994219397],[2.334862962330579,36.63912506781319],[2.333398995989152,36.638939588413535],[2.331639495989152,36.638939588413535],[2.330130755340968,36.638939588413535],[2.329340984025198,36.638857152981458],[2.328602579949478,36.63883654410963],[2.327549551528453,36.638918979563762],[2.326278212337213,36.638795326349488],[2.325340760206301,36.638424365515839],[2.32487845504585,36.638249188945714],[2.324236364545224,36.638094621053042],[2.323799743004799,36.638043098353243],[2.323529401194786,36.637895425482334],[2.323311754224323,36.638012184716828],[2.322875132683897,36.637909139172507],[2.321822104262872,36.637837007209463],[2.320422346971508,36.637795788914559],[2.318996906060119,36.637589697109227],[2.318393340989531,36.637486650999833],[2.317815459538968,36.637146597860934],[2.31690369102808,36.636713800786161],[2.316248758717441,36.63656953455429],[2.31535889102808,36.636283600786165],[2.314168385495414,36.636260391719233],[2.3126145264839,36.636384049002103],[2.311805492453111,36.636105819836558],[2.31067541317201,36.63606460061547],[2.309224288640596,36.636930199627457],[2.3081441,36.6362695],[2.3069264,36.636248],[2.3059233,36.6358778],[2.3055953,36.6358301],[2.3051849,36.6356989],[2.3048365,36.6355791],[2.3047364,36.6355037],[2.30372799395524,36.635157772172491],[2.302392445713939,36.634518863906216],[2.301188526025263,36.633529576138365],[2.297034200486235,36.63328482384302],[2.296645735733359,36.633591406995954],[2.296010066137743,36.633588830711219],[2.295592707312339,36.633660966651462],[2.295342292017096,36.633897984265339],[2.295162506676921,36.634307610813991],[2.29411910961341,36.634511135144727],[2.293627910380434,36.633995882632227],[2.29315918431498,36.63357852557138],[2.292684037344518,36.633393032818709],[2.292244205351593,36.633326049214972],[2.291903897386263,36.633545033857416],[2.291017812495404,36.633091606143275],[2.290857289870248,36.632931875290275],[2.290638979100036,36.632924146369639],[2.290481666927384,36.633022045973796],[2.290253724799663,36.633011740758164],[2.289929469096849,36.632841704501239],[2.289934284775603,36.632733499415117],[2.289704737421631,36.632667803395826],[2.28928095769122,36.632730923101683],[2.289057831242253,36.632656209974861],[2.288810626399514,36.632684549445287],[2.288765680064471,36.632769567794043],[2.288463897529178,36.632779873042068],[2.288255218116475,36.632697431019317],[2.288293743546513,36.632602107320551],[2.287661284403399,36.632416612217384],[2.287325792116824,36.632250439141636],[2.286632334376151,36.631987653081104],[2.28573340767528,36.632389560810878],[2.285540780525093,36.632126775224776],[2.285251839799813,36.631997958433693],[2.284943636359514,36.632049485175976],[2.284789534639365,36.631951584336193],[2.284449226674035,36.631930973617223],[2.28437217581396,36.631606354066435],[2.283961237893561,36.631292038595149],[2.283877766128481,36.630864361386735],[2.284019715827684,36.630013600081462],[2.283496220054032,36.629469367345145],[2.282925133755502,36.629354791542511],[2.282461126137947,36.629030159176637],[2.282127992463804,36.628734169651246],[2.281152386703816,36.62812309090598],[2.280158934496999,36.627626585857776],[2.280456375277483,36.627330590941845],[2.280581300405286,36.626920015466766],[2.280492068171141,36.626452147724265],[2.280150430772367,36.626011604645086],[2.278850195062869,36.625134464125374],[2.279028659531159,36.624757296919526],[2.279129789396524,36.624456516685797],[2.27883829743165,36.624303738974724],[2.278540856651165,36.62432283620516],[2.278302904026778,36.62449948536247],[2.277993565615074,36.624494711066248],[2.277399072977198,36.624170646184048],[2.276089208355928,36.623696550391472],[2.274496823914384,36.622810189566167],[2.273700631693613,36.621511549486847],[2.27190277829187,36.621614616959064],[2.270348919280364,36.6197387673961],[2.269843502329071,36.619591352741985],[2.26948564389005,36.619643574912544],[2.269169613060785,36.619464527323359],[2.2689847,36.6196302],[2.26851431384128,36.619389924038465],[2.268379535987623,36.619192224984381],[2.268221520572991,36.619233256905218],[2.268003087499822,36.619255637943752],[2.267831129548604,36.619266828460582],[2.2676876,36.6195882],[2.2672692,36.6201479],[2.2671297,36.6201135],[2.2670546,36.6199843],[2.2671619,36.6195796],[2.2668508,36.6196571],[2.266478703499837,36.61976293974098],[2.266274212963254,36.619986748296171],[2.266478703499837,36.620210556201613],[2.266278860475449,36.620244127331389],[2.266139435109597,36.620367221348829],[2.266013952280331,36.620445553803052],[2.26599536223155,36.620564917389764],[2.265879174426673,36.620684280791657],[2.26570256896326,36.62059475825756],[2.265614266231554,36.620445553803052],[2.265516668475458,36.620173254929163],[2.265367948085215,36.620057620869858],[2.265313739317076,36.619956124461346],[2.2653058,36.619571],[2.2652522,36.6183999],[2.2651234,36.6180037],[2.2651985,36.6175904],[2.2650483,36.6173321],[2.265179,36.6168466],[2.265415,36.6164333],[2.2658013,36.6155205],[2.2659729,36.6148488],[2.265179,36.6145732],[2.2641061,36.6145732],[2.263996,36.6147582],[2.2634691,36.6147988],[2.2626639,36.6142484],[2.2626383,36.6139769],[2.2632473,36.6136302],[2.2639267,36.6132882],[2.2644138,36.6135224],[2.2651161,36.6132191],[2.2651526,36.6117652],[2.2647381,36.6110916],[2.2638852,36.6121282],[2.2632239,36.6117105],[2.2625062,36.6112332],[2.2617366,36.6108378],[2.2599585,36.6103969],[2.2578493,36.6097192],[2.2576025,36.6095212],[2.2578187,36.6091207],[2.2584716,36.6086944],[2.2590831,36.6083413],[2.2595123,36.6083327],[2.2598341,36.6081776],[2.2597054,36.6077729],[2.2598234,36.6074886],[2.2600272,36.6077298],[2.260671,36.6076781],[2.2607353,36.6075403],[2.2606173,36.6074197],[2.2603706,36.6074456],[2.2602847,36.6073508],[2.2603491,36.6071269],[2.2604886,36.6069977],[2.260789,36.6070063],[2.2609607,36.6070666],[2.2611752,36.6073508],[2.2614005,36.607213],[2.2620175,36.6067862],[2.262409,36.6065154],[2.2623125,36.6072389],[2.2625592,36.6072217],[2.262688,36.6066532],[2.2629562,36.6068341],[2.263954,36.6067221],[2.2637609,36.6061623],[2.2632475,36.606227],[2.2627953,36.6049996],[2.2630114,36.6041944],[2.2629685,36.6036604],[2.2625914,36.6031306],[2.2626022,36.6027086],[2.2627416,36.6023899],[2.2635463,36.6020454],[2.2643831,36.6017009],[2.2646192,36.601787],[2.2642115,36.6022004],[2.2645226,36.6026224],[2.2639969,36.6028808],[2.2634497,36.6029842],[2.2635999,36.603277],[2.263557,36.6034321],[2.2636858,36.6035182],[2.2641257,36.6034062],[2.2644046,36.6034062],[2.2641793,36.603768],[2.2640613,36.6042331],[2.2643188,36.604612],[2.2646943,36.6046809],[2.2647908,36.6045173],[2.2644904,36.6042072],[2.2646943,36.6038541],[2.2648338,36.6033201],[2.2656062,36.6038369],[2.2659174,36.6034235],[2.2656813,36.603234],[2.2657135,36.6031478],[2.265456,36.6029411],[2.2654775,36.6028119],[2.2659603,36.6030445],[2.2662285,36.6030531],[2.2663573,36.6030445],[2.2665182,36.6031651],[2.2664967,36.6033201],[2.2668401,36.6033201],[2.2665826,36.6027],[2.2668186,36.6024416],[2.2662607,36.6022865],[2.2653166,36.6022693],[2.2650805,36.6014769],[2.265102,36.6008912],[2.2655526,36.5997198],[2.2661963,36.599427],[2.2662822,36.5992375],[2.2667971,36.5993408],[2.2669382,36.6004735],[2.2676554,36.6006845],[2.2682992,36.6005811],[2.2690502,36.6007362],[2.2692219,36.6006328],[2.269136,36.5996337],[2.2698227,36.5994614],[2.2705737,36.5994442],[2.2717109,36.5992202],[2.271668,36.5989274],[2.2713676,36.5988068],[2.2713891,36.598445],[2.2717539,36.5983417],[2.2724405,36.598445],[2.2727195,36.5981177],[2.2725478,36.5980144],[2.272698,36.5976181],[2.2709814,36.5978938],[2.2713676,36.5974975],[2.271947,36.5970669],[2.2732774,36.5969463],[2.273369955085797,36.596998192276196],[2.273559371783481,36.596900246923163],[2.273787313911202,36.596804878959965],[2.273728,36.5966706],[2.273711868277379,36.59649299912207],[2.273475533109521,36.596288343402904],[2.273346564646107,36.596216516162038],[2.273413953572936,36.596179203283256],[2.273539436402203,36.596184800216221],[2.273537112646105,36.596028085939636],[2.273449,36.5958437],[2.2731701,36.5957231],[2.2733203,36.5955336],[2.2736636,36.5957059],[2.273936798694882,36.595626970567515],[2.273918208646101,36.595561672518883],[2.273746250694884,36.595556075540706],[2.273577778377812,36.595466523834794],[2.273487151890008,36.595263166450003],[2.273577778377812,36.595171748735424],[2.273782268914396,36.595214659104734],[2.273778783280249,36.595347121398603],[2.274001863865613,36.595444135892102],[2.274334160987561,36.59545346420235],[2.274525870865607,36.595820065902316],[2.274472745520617,36.595955583385873],[2.274241592940393,36.596062551324785],[2.274061807600218,36.596281641821086],[2.274374826719272,36.59648784407284],[2.274509665724402,36.596444026140439],[2.274647715182036,36.59648784407284],[2.274670188349558,36.596346080083954],[2.274715134684602,36.596312572193973],[2.274824290069707,36.596459491295903],[2.274973576111103,36.596414384583838],[2.274935050681065,36.596319016020104],[2.274910972287292,36.596195294464458],[2.274955918622335,36.596103791936322],[2.274963944753593,36.595933674271649],[2.274846549207067,36.59581633459608],[2.274707123841215,36.595711857948139],[2.274595583548534,36.595737977123392],[2.274452672548535,36.595638164513161],[2.274418978085121,36.59548051629573],[2.274488690768047,36.595327531918777],[2.27466529623146,36.595193203923095],[2.274804721597312,36.595230517278686],[2.274906966865604,36.59518947258654],[2.275074277304626,36.595118577157777],[2.2752880628656,36.595133502516617],[2.275404250670476,36.595129771177177],[2.275469315841208,36.59529021861011],[2.276058709057154,36.595482602890549],[2.276373333402459,36.595539309151945],[2.276455750304612,36.595458128357066],[2.276762486109487,36.59534152440488],[2.276864731377778,36.595173614404175],[2.276976898473044,36.595327949238587],[2.2775474,36.5960504],[2.2781912,36.5960677],[2.278304420583081,36.595472292656737],[2.278156739767937,36.595353724868779],[2.277976954427763,36.595289285777163],[2.277848536327639,36.59528155308255],[2.277732960037527,36.595335681928546],[2.277649488272446,36.59535630243132],[2.277582068769881,36.59528155308255],[2.277655909177452,36.595193915822811],[2.27777790637257,36.595137209307595],[2.278002638047788,36.595121743887127],[2.278179212935459,36.595162985001508],[2.278336525108112,36.595186183118649],[2.278474574565746,36.595168140139251],[2.2788349,36.5947756],[2.2794142,36.5947756],[2.2808734,36.595034],[2.2815386,36.5954647],[2.2821608,36.595413],[2.2819677,36.5950685],[2.2818819,36.5947928],[2.2816888,36.5943966],[2.2813669,36.5945172],[2.2804871,36.5940176],[2.2798863,36.5933457],[2.280113510568585,36.592979753207523],[2.280091037401063,36.592778696878362],[2.280530869393989,36.592899846267628],[2.280701023376654,36.59245391247088],[2.281073435867016,36.592546708155361],[2.281240379397177,36.592500310327061],[2.281272483922208,36.592325029390658],[2.281118382202059,36.592020864467905],[2.281230748039668,36.591528527179321],[2.2822681,36.5915539],[2.283401013931772,36.591456351815445],[2.283683533752046,36.591693499186135],[2.284607,36.5917607],[2.2867528,36.5917607],[2.2881475,36.5913989],[2.2902718,36.5906753],[2.29015580599832,36.590157183722937],[2.2905508,36.5899344],[2.2913785,36.5897579],[2.2928376,36.5897579],[2.2941096,36.5900771],[2.2946675,36.590215],[2.2952684,36.5910936],[2.2962279,36.5921527],[2.296469747840211,36.592850800206215],[2.296641447840211,36.593350400206219],[2.297263747840211,36.593884500206215],[2.297757247840211,36.593884500206215],[2.299157914817048,36.593301957770805],[2.300210943238068,36.593136989202478],[2.300917242788753,36.593126678655246],[2.302214265600011,36.593075125898423],[2.303243,36.5930959],[2.303922226331666,36.592693634427583],[2.3036721,36.5920622],[2.3028138,36.5913903],[2.3023418,36.5905978],[2.3028353,36.5898225],[2.3038438,36.5896846],[2.3039726,36.5899431],[2.3035863,36.5903738],[2.3037151,36.5911491],[2.3041442,36.5903393],[2.304273,36.5900292],[2.3045734,36.5897019],[2.3041013,36.5890988],[2.3033288,36.5889093],[2.3026422,36.5890816],[2.3025349,36.5894607],[2.3019555,36.5895123],[2.3020414,36.588961],[2.3008826,36.5880996],[2.3009256,36.5875482],[2.300432,36.5873587],[2.2994235,36.5873759],[2.2996166,36.5878583],[2.2989729,36.5881512],[2.2978142,36.5874104],[2.2978423,36.5873567],[2.2980932,36.5868763],[2.2982219,36.5866523],[2.2968271,36.5862732],[2.2976211,36.5845847],[2.2983292,36.5850499],[2.2986511,36.5856185],[2.298694,36.5860148],[2.2997454,36.5858253],[2.2999385,36.5861354],[2.3002818,36.586032],[2.3001316,36.5852394],[2.2998956,36.5852222],[2.2997025,36.5846709],[2.3010758,36.5846019],[2.3022345,36.5851533],[2.3018783,36.5840805],[2.3010629,36.5839771],[2.3011487,36.5835808],[2.3034447,36.5840632],[2.3033374,36.5845974],[2.3042601,36.5847869],[2.3054188,36.5847007],[2.3067277,36.5844423],[2.3071783,36.5839598],[2.3075431,36.5832879],[2.3086374,36.5827537],[2.3095386,36.5830639],[2.3097623,36.5834984],[2.3118491,36.5838999],[2.312414,36.5844251],[2.3132508,36.5847352],[2.3138087,36.5845629],[2.313165,36.5838909],[2.312886,36.5837186],[2.3129504,36.5835291],[2.3140018,36.5834257],[2.3139375,36.5827537],[2.3180278,36.5815565],[2.3173841,36.5805227],[2.3174994,36.5796005],[2.3187011,36.577929],[2.3190658,36.5780669],[2.3197525,36.5787734],[2.3205555,36.5790356],[2.3217572,36.5788633],[2.3229282,36.5786528],[2.3227995,36.5795316],[2.3241942,36.5789974],[2.324559,36.5779635],[2.324838,36.5777912],[2.3254817,36.5777912],[2.3256319,36.5782048],[2.326061,36.5780497],[2.3260825,36.577481],[2.3267396,36.5767318],[2.3278554,36.5763182],[2.3303955,36.5758268],[2.3310821,36.5755338],[2.3329704,36.5761369],[2.3345154,36.5757751],[2.3360174,36.5765505],[2.3363393,36.5770158],[2.3365753,36.5764299],[2.3373263,36.5759819],[2.3375409,36.5755683],[2.3382919,36.5758612],[2.3383563,36.5755166],[2.338485,36.5752926],[2.3376696,36.5747584],[2.338013,36.5746895],[2.3385065,36.5747239],[2.3389306,36.5749599],[2.3394935,36.5753615],[2.3389142,36.575844],[2.3395365,36.5764644],[2.3382919,36.5769124],[2.3381203,36.5773776],[2.3392575,36.577998],[2.3397081,36.5779807],[2.3414247,36.577033],[2.341806,36.5766228],[2.3417738,36.5762523],[2.3421708,36.5761403],[2.3425355,36.5762264],[2.3426857,36.5761403],[2.3428467,36.5761231],[2.342954,36.5758646],[2.3427608,36.5756406],[2.3429647,36.5755286],[2.342954,36.5753218],[2.3426214,36.5753218],[2.3422137,36.5754682],[2.3418167,36.5750202],[2.341409,36.5749771],[2.3408726,36.5751236],[2.3407224,36.5748823],[2.3403254,36.5748651],[2.3402717,36.5747445],[2.3416665,36.574486],[2.3426106,36.5742878],[2.3431363,36.5739949],[2.3434475,36.5737278],[2.3438659,36.573633],[2.3444345,36.5733659],[2.3446384,36.5736072],[2.3448851,36.5734521],[2.3447671,36.5731246],[2.3448422,36.5728058],[2.3450511,36.5727077],[2.3461669,36.5722424],[2.346875,36.5723114],[2.3474635,36.5726943],[2.3477484,36.5721434],[2.3479791,36.571984],[2.3483935,36.5717633],[2.3488226,36.5717719],[2.3487629,36.5722676],[2.3491217,36.572626],[2.3498888,36.5728241],[2.3510154,36.5729965],[2.351525,36.5730783],[2.3519595,36.5731688],[2.352335,36.5733067],[2.3523618,36.5732119],[2.3520078,36.5726475],[2.3519327,36.5724407],[2.3520829,36.5722081],[2.3523833,36.5721564],[2.3528285,36.5721133],[2.353086,36.5720357],[2.3537727,36.5718203],[2.3545237,36.5716265],[2.3545934,36.5718246],[2.3549529,36.5717816],[2.3550333,36.5716782],[2.3551835,36.5713938],[2.3552586,36.5714929],[2.3553981,36.57148],[2.3557039,36.571256],[2.354926,36.5712215],[2.3549904,36.5710147],[2.3547758,36.5709458],[2.3550172,36.5707605],[2.3568981,36.5709156],[2.3558606,36.5731837],[2.3557076,36.5748054],[2.3568057,36.5768062],[2.359671,36.5752297],[2.3603601,36.5743236],[2.3619328,36.5741256],[2.3633185,36.5723255],[2.3628814,36.571555],[2.3627259,36.5697954],[2.364594,36.569971],[2.3650124,36.5703588],[2.3654845,36.570376],[2.3660733,36.5698644],[2.3667814,36.5691233],[2.3672964,36.5691923],[2.3682015,36.5693154],[2.3681547,36.5699161],[2.3713153,36.5696747],[2.3724525,36.5693817],[2.3726027,36.5688303],[2.3733538,36.5688475],[2.3732465,36.5692956],[2.3738687,36.5695368],[2.3743408,36.5692266],[2.3742335,36.5689509],[2.3767966,36.5691443],[2.3768648,36.5691494],[2.3781174,36.5692956],[2.3780744,36.5697436],[2.3799198,36.5701745],[2.3837178,36.5711395],[2.3855846,36.5719667],[2.385515,36.5720425],[2.3854077,36.5721305],[2.3853755,36.572277],[2.3852842,36.5722941],[2.3845761,36.5722424],[2.3841255,36.5717082],[2.3833316,36.5716393],[2.3831385,36.5721563],[2.3833959,36.5721907],[2.3832457,36.5725526],[2.3833959,36.5729145],[2.3833907,36.5732162],[2.3839753,36.5732764],[2.3844903,36.5734143],[2.3850966,36.5736642],[2.3856919,36.5740002],[2.3855417,36.5742759],[2.3861854,36.5747928],[2.3864215,36.5751547],[2.3873012,36.5753443],[2.3876017,36.5750513],[2.3885458,36.5751547],[2.3880523,36.5743965],[2.3895328,36.574431],[2.3895758,36.5742156],[2.3898118,36.574138],[2.3900264,36.5740734],[2.3920096,36.5751068],[2.3932584,36.5757668],[2.3940448,36.5764585],[2.3950475,36.5764988],[2.3953693,36.5761542],[2.3960774,36.5764988],[2.3954981,36.5772915],[2.3955195,36.577929],[2.395262,36.5786183],[2.3945754,36.5783771],[2.3932665,36.5786872],[2.3922365,36.5787562],[2.3914426,36.5797383],[2.3918074,36.579859],[2.391743,36.5804448],[2.3918932,36.580531],[2.3918932,36.5809962],[2.3926227,36.5809617],[2.3933523,36.5802725],[2.3938458,36.5801346],[2.39479,36.5801346],[2.3948758,36.5798762],[2.3962062,36.57979],[2.3972361,36.5802208],[2.3976868,36.580686],[2.3993934,36.5814539],[2.4003375,36.5821087],[2.4012173,36.5826256],[2.4013775,36.5832362],[2.4017537,36.5835043],[2.4039424,36.5832286],[2.404157,36.5825739],[2.4045647,36.5819019],[2.4044789,36.5814022],[2.4042643,36.5807302],[2.4045003,36.5807474],[2.4048866,36.5813333],[2.4051226,36.5812988],[2.4049509,36.580868],[2.4055088,36.5810059],[2.4063671,36.5807474],[2.4071201,36.5804193],[2.4068526,36.5801715],[2.4064664,36.5800423],[2.4064986,36.5798442],[2.4061552,36.5795771],[2.4061767,36.5791894],[2.4056832,36.5790343],[2.404631,36.5794888],[2.404678055635014,36.579688652580685],[2.404505539982333,36.579784193925171],[2.404356819592091,36.579774639796035],[2.404327075514042,36.57949756953704],[2.40428840821258,36.579501152348463],[2.404203637590142,36.579553700230171],[2.404045993976485,36.579689846848218],[2.403880914343317,36.579812856305452],[2.403819938983317,36.579780611126871],[2.403824400595024,36.579700595255211],[2.403934453683804,36.579632521985673],[2.404156047065265,36.579392473661457],[2.4041785,36.5791449],[2.4039443,36.5783516],[2.4038225,36.5780798],[2.4037367,36.5777265],[2.4036294,36.5775951],[2.403506,36.5776468],[2.4033987,36.5775671],[2.4033532,36.5775004],[2.4033773,36.5774293],[2.4034899,36.5774207],[2.403445857910152,36.577330679184307],[2.403410957910152,36.577216479184308],[2.403410957910152,36.577076479184306],[2.403443157910152,36.57697527918431],[2.403408257910152,36.576818079184306],[2.4035543,36.5768025],[2.4035999,36.5767163],[2.403675,36.5768456],[2.4038815,36.5768003],[2.4039915,36.5769145],[2.4038762,36.5769145],[2.4037528,36.5769985],[2.403734,36.5771191],[2.4037608,36.5772871],[2.4038869,36.5774465],[2.4039781,36.5776835],[2.4041176,36.577929],[2.4044019,36.5782176],[2.4052728,36.5778353],[2.4063215,36.5780779],[2.4067561,36.5780521],[2.4069438,36.5779056],[2.4077431,36.5779746],[2.4080489,36.5780823],[2.407845,36.5786294],[2.409508,36.5797365],[2.4097226,36.5793574],[2.4094544,36.5791075],[2.4095187,36.5789395],[2.4104951,36.5797494],[2.4109457,36.5802232],[2.4112032,36.5806497],[2.4115787,36.5810546],[2.4111777,36.5812797],[2.4110516,36.5813702],[2.4110007,36.5814596],[2.4110133,36.5814896],[2.4110261,36.5815199],[2.4111965,36.5819549],[2.4113896,36.5825063],[2.4114073,36.583171],[2.4105527,36.5835229],[2.4102845,36.5833678],[2.4096837,36.5837297],[2.409276,36.5837124],[2.408146215135461,36.583492301009535],[2.407592975283761,36.583659490047211],[2.407271739240838,36.583946098983652],[2.407479947787176,36.584313912226328],[2.407075428325718,36.58471993779672],[2.407349073843763,36.584987435829028],[2.407378817921812,36.58535524410987],[2.407289585687667,36.585379127703874],[2.407140865297424,36.585293146730884],[2.407158711744253,36.585087747352162],[2.406896963857427,36.584901454419743],[2.406706601757917,36.584944445136365],[2.406492444395969,36.58507341714256],[2.406563830183285,36.585164175091812],[2.40665306241743,36.585259709659958],[2.406569778998895,36.58532180706586],[2.406397263346214,36.585269263110277],[2.406296133480849,36.585135514698322],[2.406076027303291,36.58482980317217],[2.4044593,36.5852094],[2.4031659,36.5856034],[2.401899958745292,36.5856084098303],[2.401810726511147,36.585742157422864],[2.401519234546273,36.585813807823556],[2.40118610087213,36.585938001693862],[2.400888660091646,36.585914118272783],[2.400638809836038,36.585818584514577],[2.400445709836038,36.585801284514574],[2.400274009836038,36.585728084514571],[2.400091518799947,36.585498545563034],[2.399788129203854,36.585350467390178],[2.3994859,36.5851404],[2.3989436,36.5850216],[2.3986754,36.5850044],[2.3983755,36.5849875],[2.398152204911189,36.585147456530201],[2.39814625609558,36.585355244109842],[2.398250360368748,36.585426894869663],[2.398387183127771,36.585426894869663],[2.398482364177529,36.585518846580712],[2.398806103761893,36.585593341134597],[2.399014783174596,36.585717079766901],[2.399084854202663,36.585988871784821],[2.399242166375315,36.586024962031743],[2.399540738458104,36.585929580628232],[2.399797574658353,36.58590637972847],[2.400301615701342,36.585955359397559],[2.40081528810184,36.586079097370479],[2.4011865,36.5864477],[2.4013259,36.5867147],[2.4018624,36.5868784],[2.402985553993945,36.587074149691311],[2.40387805978981,36.586986503110879],[2.404565096625476,36.586744185576464],[2.405521811471405,36.586929790564618],[2.405708017716585,36.587275220882113],[2.406234531927095,36.587285532211112],[2.4072488,36.587587],[2.4093474,36.5883055],[2.4096478,36.5888224],[2.4091575,36.5891717],[2.4091816,36.5892364],[2.4091306,36.5893591],[2.4090233,36.5894345],[2.4089187,36.5895314],[2.4090958,36.5896434],[2.409195,36.5897231],[2.4092326,36.58982],[2.4092621,36.5899255],[2.4092621,36.5900806],[2.4093559,36.5901344],[2.4094498,36.590128],[2.4095705,36.5900935],[2.4096322,36.5901107],[2.4097127,36.5901926],[2.4097931,36.5902378],[2.4097529,36.590283],[2.4096054,36.5902636],[2.4094605,36.5902787],[2.4092862,36.5902636],[2.4091682,36.5902529],[2.4091119,36.5902098],[2.4091172,36.5901301],[2.4091092,36.5899535],[2.4090448,36.5897941],[2.4089214,36.5896692],[2.4088141,36.5896111],[2.4085486,36.589456],[2.4083367,36.5894474],[2.4080551,36.5894819],[2.4078899,36.5894327],[2.4075374,36.5893527],[2.407259,36.5893638],[2.4069715,36.5894366],[2.4068615,36.58954],[2.4068513,36.5896738],[2.4069908,36.5899883],[2.4069827,36.5903092],[2.4068266,36.590311],[2.4065208,36.5906319],[2.4067944,36.5908193],[2.4068829,36.5907439],[2.4070144,36.590759],[2.4071377,36.591278],[2.4073067,36.5913081],[2.407627924575468,36.59178384379603],[2.407859928384246,36.591826830679281],[2.408020546405709,36.591900863588748],[2.408032444036927,36.59206564626129],[2.408474699958878,36.592139195988672],[2.40872845546326,36.592232816728966],[2.4090636,36.5921179],[2.4090448,36.5920102],[2.40899317775789,36.591972508272214],[2.408972356903257,36.591908028060075],[2.40909133321545,36.591915192530749],[2.409180565449596,36.591915192530749],[2.4092594,36.5919499],[2.4093693,36.5919326],[2.4093854,36.5920705],[2.409424466889595,36.59203937658345],[2.409424466889595,36.591960567496258],[2.409406620442765,36.591867429380372],[2.4094552,36.591825],[2.4094391,36.5917388],[2.4095035,36.5916958],[2.4095866,36.5917108],[2.4096107,36.5918422],[2.4096376,36.59198],[2.4096054,36.5920683],[2.4098387,36.5920855],[2.410233,36.5920899],[2.4103376,36.5920511],[2.4103269,36.5921372],[2.4103457,36.5922105],[2.4103001,36.5922492],[2.4102062,36.5922363],[2.4100614,36.5922126],[2.4098629,36.5922428],[2.4095598,36.5922944],[2.4093854,36.5922492],[2.409195,36.5922686],[2.4090421,36.5923483],[2.4091902,36.5926759],[2.4099063,36.5930862],[2.4100184,36.5932043],[2.4101298,36.593284],[2.4102156,36.5933411],[2.410178,36.5933798],[2.4101485,36.5934164],[2.4101526,36.5934703],[2.4102075,36.5935715],[2.410233,36.5936932],[2.4102335,36.5938194],[2.4100989,36.593957],[2.4101526,36.5942025],[2.4102102,36.5944253],[2.4102357,36.5946353],[2.410237,36.5947688],[2.4101914,36.594842],[2.4101163,36.5948711],[2.410064,36.5948367],[2.4101123,36.5947699],[2.4100667,36.5946644],[2.4098213,36.5944749],[2.4096389,36.5943252],[2.4095536,36.5942319],[2.4094391,36.5941831],[2.4092889,36.5941605],[2.4090368,36.5941841],[2.4081963,36.594326],[2.4080958,36.5943385],[2.4078276,36.594459],[2.406559368571559,36.594643762672966],[2.406587625445722,36.595027495093113],[2.406308031112067,36.595170778587892]])