NAME = 'Test'
ART = 'art-default.jpg'
ICON = 'icon-default.png'

###################################################################################################
def Start():

	Plugin.AddPrefixHandler('/video/test', MainMenu, NAME, ICON, ART)
	Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')

	ObjectContainer.title1 = NAME
	ObjectContainer.view_group = 'InfoList'
	ObjectContainer.art = R(ART)

	VideoClipObject.thumb = R(ICON)

	HTTP.CacheTime = 0

###################################################################################################
def MainMenu():

	oc = ObjectContainer(view_group='InfoList')

	oc.add(
		VideoClipObject(
			title = 'Test video',
			key = 'http://dl.dropbox.com/u/2974527/fringe.flv',
			rating_key = 'http://dl.dropbox.com/u/2974527/fringe.flv',
			items = [
				MediaObject(
					parts = [
						PartObject(
							key = 'http://dl.dropbox.com/u/2974527/fringe.flv'
						)
					]
				)
			]
		)
	)

	return oc
