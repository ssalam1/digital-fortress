from hunt import settings
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django import forms
from player.models import userInfo
from level.models import level
from django.utils.safestring import mark_safe
from fandjango.decorators import facebook_authorization_required
from facepy import GraphAPI
import random

@facebook_authorization_required
def level_view(request,slug):
	
	curr_level = level.objects.get(slug = slug)
	ui = userInfo.objects.get(user = request.facebook.user)
	if ui.max_level < curr_level.number:
		redirect_level = level.objects.get(number = ui.max_level)
		return HttpResponseRedirect('/level/'+redirect_level.slug+'/')
	else:
		number = curr_level.number
		title = curr_level.title
		source = curr_level.source
		photo = curr_level.photo
		text = curr_level.text
		js = curr_level.js
		l = curr_level.number
		player_name = request.facebook.user.first_name
		user_list = userInfo.objects.all()
		count = 0
		for u in user_list:
			if u.max_level> curr_level.number:
				count+=1
			
		return render_to_response('level.html',{'title':title,'number':number,'source':mark_safe(source),'photo':photo,'text':mark_safe(text),'js':mark_safe(js),'level':l,'name':player_name,'pass_count':str(count)},context_instance=RequestContext(request))

def level_file(request,filename):
	return HttpResponseRedirect('/static/'+filename)
		

def level_scrape(request):
	messages = {'264717': 'add 21435', '118842': 'subtract 22630', '145755': 'add 12706', '170520': 'add 15794', '174196': 'add 6077', '122433': 'add 20845', '60469': 'subtract 24308', '46333': 'add 15797', '46974': 'add 18333', '113623': 'subtract 8756', '288450': 'add 10954', '105824': 'add 10155', '139783': 'subtract 21122', '312652': 'add 22913', '189464': 'subtract 23373', '172427': 'add 8271', '344734': 'subtract 9548', '122345': 'add 19710', '335426': 'subtract 15371', '160119': 'subtract 24439', '180199': 'subtract 7772', '277856': 'subtract 5681', '77961': 'add 22760', '461127': 'add 17951', '327789': 'add 11886', '197712': 'subtract 9294', '96379': 'subtract 8052', '166091': 'add 18737', '470727': 'subtract 13754', '439053': 'subtract 5288', '335186': 'add 8552', '479078': 'subtract 5809', '128493': 'add 14948', '146447': 'subtract 5447', '164217': 'add 11950', '145927': 'add 15405', '180293': 'add 9665', '180698': 'subtract 14128', '433765': 'subtract 24215', '339437': 'add 18301', '478309': 'subtract 7582', '129793': 'add 21499', '114273': 'subtract 6557', '404120': 'subtract 23730', '181246': 'subtract 10972', '167944': 'add 12349', '180273': 'subtract 21958', '98367': 'add 7802', '202218': 'subtract 24438', '357854': 'add 7806', '85526': 'add 24012', '202110': 'subtract 6028', '158315': 'add 12145', '406755': 'add 15710', '326644': 'subtract 22151', '178979': 'add 10890', '443392': 'add 17735', '286152': 'subtract 20952', '177967': 'subtract 15057', '376095': 'add 17912', '197729': 'subtract 18750', '188815': 'subtract 23424', '165498': 'subtract 10067', '307374': 'subtract 18988', '62130': 'add 14726', '83627': 'subtract 5666', '285253': 'add 20474', '155913': 'add 15642', '83780': 'subtract 16138', '347436': 'add 9554', '406754': 'add 15003', '129485': 'subtract 23156', '196082': 'subtract 7267', '55994': 'subtract 9661', '286831': 'add 20506', '316689': 'add 15600', '142055': 'subtract 9053', '161288': 'add 14365', '413176': 'subtract 6421', '359452': 'subtract 10615', '380390': 'subtract 20938', '169017': 'subtract 24760', '162910': 'add 18336', '173083': 'subtract 7846', '94234': 'add 21199', '394007': 'add 24520', '48374': 'add 22038', '48932': 'add 23253', '192007': 'add 10103', '80598': 'subtract 5260', '184070': 'add 20092', '118557': 'subtract 12733', '115979': 'subtract 12462', '37532': 'add 18462', '128574': 'add 24993', '107944': 'subtract 13115', '91221': 'add 22660', '121731': 'subtract 23395', '350833': 'add 7021', '182690': 'add 8087', '184828': 'add 17390', '439585': 'subtract 7532', '94829': 'subtract 10579', '188939': 'add 18566', '154572': 'add 23395', '175653': 'subtract 19740', '343969': 'subtract 16180', '79219': 'add 17160', '96123': 'subtract 12343', '386453': 'add 10228', '156051': 'subtract 22305', '152361': 'add 20722', '347962': 'add 21249', '324682': 'subtract 19477', '69105': 'subtract 20173', '272175': 'subtract 13577', '144366': 'subtract 12532', '131998': 'add 13929', '70412': 'subtract 6102', '153651': 'add 11847', '73762': 'add 9865', '434328': 'add 19448', '76856': 'add 24256', '299404': 'add 13248', '124691': 'add 21756', '182284': 'subtract 14285', '145171': 'subtract 22826', '67642': 'subtract 19268', '453776': 'subtract 19139', '362349': 'add 16868', '118661': 'subtract 5038', '195894': 'add 7978', '100721': 'subtract 9190', '203872': 'subtract 19802', '61966': 'subtract 5396', '153886': 'subtract 13595', '377943': 'add 21812', '399755': 'add 6999', '103517': 'subtract 17454', '91531': 'subtract 22615', '54623': 'add 9184', '170460': 'add 9739', '133002': 'add 12753', '343738': 'add 20565', '250165': 'add 14552', '369211': 'add 17242', '170274': 'subtract 14030', '374309': 'subtract 7816', '171352': 'subtract 10648', '167999': 'add 20940', '88327': 'subtract 14565', '131834': 'subtract 16302', '115433': 'add 6965', '106329': 'add 13917', '107527': 'subtract 5305', '120246': 'subtract 21879', '456436': 'subtract 11350', '353481': 'add 14309', '143044': 'subtract 14470', '156244': 'subtract 16461', '65307': 'subtract 15600', '173710': 'subtract 17659', '72185': 'add 12445', '135680': 'add 18892', '367790': 'subtract 5441', '434075': 'subtract 17776', '304493': 'add 20189', '359560': 'subtract 12124', '133746': 'add 13572', '151292': 'add 16652', '189869': 'subtract 16159', '44641': 'add 10828', '363935': 'subtract 15973', '450565': 'subtract 11512', '147318': 'add 24034', '140291': 'add 20997', '72676': 'add 7922', '285687': 'subtract 12116', '115725': 'subtract 8198', '171555': 'add 11295', '141291': 'add 22926', '258598': 'add 17239', '14625': 'add 22907', '82871': 'add 8350', '55469': 'add 24083', '432053': 'add 11339', '445086': 'subtract 5501', '305205': 'subtract 16755', '117185': 'subtract 11105', '360095': 'add 17848', '316000': 'add 10644', '212439': 'subtract 9189', '176167': 'subtract 7142', '107716': 'add 23614', '307337': 'subtract 22084', '294034': 'add 13340', '320055': 'add 19240', '409550': 'great! the answer is bazinga!', '105318': 'add 24167', '165237': 'subtract 13123', '49707': 'add 19398', '366493': 'subtract 6398', '122673': 'subtract 23440', '198990': 'subtract 24794', '422465': 'add 18236', '56570': 'subtract 11929', '202377': 'subtract 20121', '102222': 'add 14963', '161332': 'subtract 13347', '207505': 'add 9559', '335565': 'add 23995', '158461': 'add 12059', '115532': 'subtract 10214', '456973': 'subtract 22645', '75338': 'subtract 13372', '256940': 'add 20916', '106169': 'add 16264', '186314': 'add 12676', '188418': 'add 24021', '143667': 'subtract 18976', '196859': 'add 17980', '379217': 'subtract 15282', '144257': 'subtract 14464', '203250': 'subtract 11243', '348837': 'subtract 22128', '424689': 'subtract 20569', '109538': 'subtract 13415', '99233': 'subtract 20014', '217064': 'subtract 20205', '68916': 'subtract 21942', '166570': 'add 11788', '289581': 'add 24907', '152114': 'add 16903', '311399': 'subtract 21818', '160704': 'add 15490', '421757': 'add 12318', '359514': 'subtract 15545', '402458': 'add 21990', '364303': 'subtract 13470', '473269': 'add 5040', '214839': 'add 10949', '143441': 'add 10210', '273571': 'add 13260', '134882': 'subtract 16325', '339675': 'add 13806', '164138': 'subtract 21094', '182256': 'add 15456', '96212': 'add 19513', '86063': 'add 21881', '131330': 'subtract 8657', '356990': 'subtract 21564', '36161': 'subtract 21536', '182850': 'subtract 18712', '288386': 'add 11246', '178358': 'add 10979', '101112': 'subtract 18241', '143278': 'add 16841', '440701': 'add 9864', '84630': 'subtract 11954', '176194': 'subtract 6974', '104867': 'add 13975', '63807': 'add 21719', '165391': 'subtract 7056', '155431': 'subtract 11764', '106080': 'add 22413', '153567': 'subtract 12276', '299632': 'subtract 13945', '418527': 'subtract 5351', '169220': 'add 13064', '190777': 'subtract 23532', '64310': 'subtract 12945', '122398': 'add 9600', '339295': 'add 5439', '396681': 'subtract 22372', '225788': 'add 24377', '305727': 'add 10273', '169025': 'subtract 23854', '84250': 'add 9984', '424448': 'add 9264', '314488': 'add 24949', '275837': 'add 18197', '332289': 'subtract 20890', '177780': 'add 24597', '204162': 'subtract 21472', '51365': 'add 9104', '189958': 'add 5936', '326709': 'subtract 10020', '365660': 'subtract 6146', '158335': 'subtract 13969', '113881': 'add 21001', '416299': 'subtract 13841', '189337': 'add 8392', '265200': 'subtract 8260', '98336': 'add 15937', '79552': 'subtract 24929', '433712': 'add 22724', '434637': 'subtract 9948', '141000': 'subtract 19269', '147985': 'add 5901', '167245': 'add 22219', '357738': 'add 18357'}
	try:
		return HttpResponse(messages[str(request.GET['score'])])
	except:
		return HttpResponse(random.choice(['add','subtract']) + " " + str(random.randint(596859,928756)))
@facebook_authorization_required
def check_answer(request):

	given_answer = request.POST['answer']
	user_level = request.POST['level']
	curr_level = level.objects.get(number = user_level)
	if curr_level.answer == given_answer:
		token =	request.facebook.user.oauth_token.token
		graph = GraphAPI(token)
		profile_id = request.facebook.user.facebook_id
		try:
			graph.post(path = str(profile_id)+'/feed', message = 'I just crossed level ' +str(user_level) + '!! in MUKTI\'s Digital Fortress. Join me!', caption = 'Digital Fortress' , link = 'digitalfortress.mkti.in')
		except:
			pass
		ui = userInfo.objects.get(user = request.facebook.user)
		ui.max_level = curr_level.number + 1
		ui.save()
		try:
			next_level = level.objects.get(number = curr_level.number + 1)
		except:
			return HttpResponse('Adding More Levels. Stay Tuned')
		return HttpResponseRedirect('/level/'+next_level.slug+'/')
	else:
		return HttpResponseRedirect(request.META['HTTP_REFERER'])
		

	
	
