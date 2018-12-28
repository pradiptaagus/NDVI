# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NDVI\n", pos = wx.DefaultPosition, size = wx.Size( 1385,672 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RED" ), wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 180,180 ), 0 )
		self.m_bitmap2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		sbSizer4.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_filePickerRed = wx.FilePickerCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 200,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer4.Add( self.m_filePickerRed, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_button5 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_button5.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		sbSizer4.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer8.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NIR" ), wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 180,180 ), 0 )
		self.m_bitmap3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		sbSizer5.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_filePickerNir = wx.FilePickerCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 200,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer5.Add( self.m_filePickerNir, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_button6.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		sbSizer5.Add( self.m_button6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer8.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_bitmap10 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"file.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_bitmap10, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Import MTL. file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		fgSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		bSizer71.Add( fgSizer4, 0, wx.TOP, 5 )
		
		self.m_filePicker3 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer71.Add( self.m_filePicker3, 1, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer71, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_bitmap8 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"crop.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_bitmap8, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Crop coordinate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		fgSizer2.Add( self.m_staticText19, 0, wx.ALIGN_TOP|wx.ALL, 5 )
		
		
		bSizer10.Add( fgSizer2, 0, 0, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Default coordinate" ), wx.VERTICAL )
		
		gSizer21 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText141 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Logitude start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		self.m_staticText141.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer21.Add( self.m_staticText141, 0, wx.ALL, 5 )
		
		self.m_staticText152 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"No set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )
		gSizer21.Add( self.m_staticText152, 0, wx.ALL, 5 )
		
		self.m_staticText151 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Latitude start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		self.m_staticText151.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer21.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Not set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gSizer21.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_staticText161 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Logitude end", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		self.m_staticText161.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer21.Add( self.m_staticText161, 0, wx.ALL, 5 )
		
		self.m_staticText162 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Not set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )
		gSizer21.Add( self.m_staticText162, 0, wx.ALL, 5 )
		
		self.m_staticText171 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Longitude end", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )
		self.m_staticText171.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer21.Add( self.m_staticText171, 0, wx.ALL, 5 )
		
		self.m_staticText172 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Not set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )
		gSizer21.Add( self.m_staticText172, 0, wx.ALL, 5 )
		
		
		sbSizer10.Add( gSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( sbSizer10, 1, wx.EXPAND, 5 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Crop coordinate" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText14 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Longitude start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer2.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl14, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Latitude start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer2.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl15, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Logitude end", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer2.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_textCtrl16 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl16, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Latidtude end", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gSizer2.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_textCtrl17 = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_textCtrl17, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer12.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"START CROP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		
		bSizer12.Add( self.m_button8, 0, wx.ALL, 5 )
		
		self.m_button91 = wx.Button( self, wx.ID_ANY, u"START CORRECTION", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button91.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_button91.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
		
		bSizer12.Add( self.m_button91, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Radiance Correction" ), wx.HORIZONTAL )
		
		sbSizer72 = wx.StaticBoxSizer( wx.StaticBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"RED" ), wx.VERTICAL )
		
		self.m_bitmap42 = wx.StaticBitmap( sbSizer72.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 180,180 ), 0 )
		self.m_bitmap42.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		sbSizer72.Add( self.m_bitmap42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer73 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonSave2 = wx.Button( sbSizer72.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSave2.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_buttonSave2.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		self.m_buttonSave2.SetMaxSize( wx.Size( 250,-1 ) )
		
		bSizer73.Add( self.m_buttonSave2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer72.Add( bSizer73, 1, wx.EXPAND, 5 )
		
		
		sbSizer9.Add( sbSizer72, 1, wx.EXPAND, 5 )
		
		sbSizer711 = wx.StaticBoxSizer( wx.StaticBox( sbSizer9.GetStaticBox(), wx.ID_ANY, u"NIR" ), wx.VERTICAL )
		
		self.m_bitmap411 = wx.StaticBitmap( sbSizer711.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 180,180 ), 0 )
		self.m_bitmap411.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		sbSizer711.Add( self.m_bitmap411, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer721 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonSave11 = wx.Button( sbSizer711.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSave11.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_buttonSave11.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		self.m_buttonSave11.SetMaxSize( wx.Size( 250,-1 ) )
		
		bSizer721.Add( self.m_buttonSave11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer711.Add( bSizer721, 1, wx.EXPAND, 5 )
		
		
		sbSizer9.Add( sbSizer711, 1, wx.EXPAND, 5 )
		
		
		bSizer11.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Reflectence Correction" ), wx.HORIZONTAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"RED" ), wx.VERTICAL )
		
		self.m_bitmap4 = wx.StaticBitmap( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 180,180 ), 0 )
		self.m_bitmap4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		sbSizer7.Add( self.m_bitmap4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonSave = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSave.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_buttonSave.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		self.m_buttonSave.SetMaxSize( wx.Size( 250,-1 ) )
		
		bSizer7.Add( self.m_buttonSave, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer7.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		sbSizer6.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		sbSizer71 = wx.StaticBoxSizer( wx.StaticBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"NIR" ), wx.VERTICAL )
		
		self.m_bitmap41 = wx.StaticBitmap( sbSizer71.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 180,180 ), 0 )
		self.m_bitmap41.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		sbSizer71.Add( self.m_bitmap41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer72 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonSave1 = wx.Button( sbSizer71.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSave1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_buttonSave1.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		self.m_buttonSave1.SetMaxSize( wx.Size( 250,-1 ) )
		
		bSizer72.Add( self.m_buttonSave1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer71.Add( bSizer72, 1, wx.EXPAND, 5 )
		
		
		sbSizer6.Add( sbSizer71, 1, wx.EXPAND, 5 )
		
		
		bSizer11.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"START NDVI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_button10.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		
		bSizer141.Add( self.m_button10, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer141, 0, wx.EXPAND, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NDVI Result" ), wx.VERTICAL )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap11 = wx.StaticBitmap( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), 0 )
		self.m_bitmap11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bSizer15.Add( self.m_bitmap11, 0, wx.ALL, 5 )
		
		
		sbSizer8.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		self.m_button9 = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 128, 255, 128 ) )
		
		sbSizer8.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( sbSizer8, 0, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer9, 1, wx.LEFT, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePickerRed.Bind( wx.EVT_FILEPICKER_CHANGED, self.filePickerRedChanged )
		self.m_button5.Bind( wx.EVT_BUTTON, self.onCLickSaveRed )
		self.m_filePickerNir.Bind( wx.EVT_FILEPICKER_CHANGED, self.filePickerNirChanged )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onClickSaveNir )
		self.m_filePicker3.Bind( wx.EVT_FILEPICKER_CHANGED, self.importMtlChanged )
		self.m_button8.Bind( wx.EVT_BUTTON, self.onStartCrop )
		self.m_button91.Bind( wx.EVT_BUTTON, self.onStartCorrection )
		self.m_buttonSave2.Bind( wx.EVT_BUTTON, self.onSaveRadianceRed )
		self.m_buttonSave11.Bind( wx.EVT_BUTTON, self.onSaveRadianceNir )
		self.m_buttonSave.Bind( wx.EVT_BUTTON, self.onSaveReflectenceRed )
		self.m_buttonSave1.Bind( wx.EVT_BUTTON, self.onSaveReflectenceNir )
		self.m_button10.Bind( wx.EVT_BUTTON, self.onStartNdvi )
		self.m_button9.Bind( wx.EVT_BUTTON, self.onClickSaveResult )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def filePickerRedChanged( self, event ):
		event.Skip()
	
	def onCLickSaveRed( self, event ):
		event.Skip()
	
	def filePickerNirChanged( self, event ):
		event.Skip()
	
	def onClickSaveNir( self, event ):
		event.Skip()
	
	def importMtlChanged( self, event ):
		event.Skip()
	
	def onStartCrop( self, event ):
		event.Skip()
	
	def onStartCorrection( self, event ):
		event.Skip()
	
	def onSaveRadianceRed( self, event ):
		event.Skip()
	
	def onSaveRadianceNir( self, event ):
		event.Skip()
	
	def onSaveReflectenceRed( self, event ):
		event.Skip()
	
	def onSaveReflectenceNir( self, event ):
		event.Skip()
	
	def onStartNdvi( self, event ):
		event.Skip()
	
	def onClickSaveResult( self, event ):
		event.Skip()
	

