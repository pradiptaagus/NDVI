# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import self as self
import wx
import wx.xrc
from NDVI import NDVI
from PIL import Image


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"NDVI\n", pos=wx.DefaultPosition, size=wx.Size(1180, 690),
						  style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

		bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer10 = wx.BoxSizer(wx.VERTICAL)

		bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

		sbSizer9 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Original"), wx.HORIZONTAL)

		sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(sbSizer9.GetStaticBox(), wx.ID_ANY, u"RED"), wx.VERTICAL)

		self.m_bitmap2 = wx.StaticBitmap(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
										 wx.Size(250, 250), 0)
		self.m_bitmap2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		sbSizer4.Add(self.m_bitmap2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_filePickerRed = wx.FilePickerCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file",
												 u"*.*", wx.DefaultPosition, wx.Size(200, -1), wx.FLP_DEFAULT_STYLE)
		sbSizer4.Add(self.m_filePickerRed, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

		self.m_button5 = wx.Button(sbSizer4.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button5.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))
		self.m_button5.SetBackgroundColour(wx.Colour(128, 255, 128))

		sbSizer4.Add(self.m_button5, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

		sbSizer9.Add(sbSizer4, 1, wx.EXPAND, 5)

		sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(sbSizer9.GetStaticBox(), wx.ID_ANY, u"NIR"), wx.VERTICAL)

		self.m_bitmap3 = wx.StaticBitmap(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
										 wx.Size(250, 250), 0)
		self.m_bitmap3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		sbSizer5.Add(self.m_bitmap3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_filePickerNir = wx.FilePickerCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file",
												 u"*.*", wx.DefaultPosition, wx.Size(200, -1), wx.FLP_DEFAULT_STYLE)
		sbSizer5.Add(self.m_filePickerNir, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

		self.m_button6 = wx.Button(sbSizer5.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button6.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))
		self.m_button6.SetBackgroundColour(wx.Colour(128, 255, 128))

		sbSizer5.Add(self.m_button6, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

		sbSizer9.Add(sbSizer5, 1, wx.EXPAND, 5)

		bSizer8.Add(sbSizer9, 1, wx.EXPAND, 5)

		bSizer10.Add(bSizer8, 1, wx.EXPAND, 5)

		bSizer12 = wx.BoxSizer(wx.VERTICAL)

		bSizer71 = wx.BoxSizer(wx.HORIZONTAL)

		fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer4.SetFlexibleDirection(wx.BOTH)
		fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_bitmap10 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"file.png", wx.BITMAP_TYPE_ANY),
										  wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer4.Add(self.m_bitmap10, 0, wx.ALL, 5)

		self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Import MTL. file", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText7.Wrap(-1)
		self.m_staticText7.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))

		fgSizer4.Add(self.m_staticText7, 0, wx.ALL, 5)

		bSizer71.Add(fgSizer4, 0, wx.TOP | wx.EXPAND, 5)

		self.m_filePicker3 = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
											   wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
		bSizer71.Add(self.m_filePicker3, 1, wx.ALL | wx.EXPAND, 5)

		bSizer12.Add(bSizer71, 1, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)

		bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer12.Add(bSizer15, 1, wx.EXPAND, 5)

		bSizer10.Add(bSizer12, 0, wx.EXPAND, 5)

		fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer2.SetFlexibleDirection(wx.BOTH)
		fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_bitmap8 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"crop.png", wx.BITMAP_TYPE_ANY),
										 wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer2.Add(self.m_bitmap8, 0, wx.ALL, 5)

		self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"Crop coordinate", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText19.Wrap(-1)
		self.m_staticText19.SetFont(wx.Font(12, 74, 90, 90, False, "Arial"))

		fgSizer2.Add(self.m_staticText19, 0, wx.ALIGN_TOP | wx.ALL, 5)

		bSizer10.Add(fgSizer2, 0, wx.EXPAND, 5)

		bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

		sbSizer10 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Default coordinate"), wx.VERTICAL)

		gSizer21 = wx.GridSizer(0, 2, 0, 0)

		self.m_staticText141 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"Logitude start", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.m_staticText141.Wrap(-1)
		self.m_staticText141.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer21.Add(self.m_staticText141, 0, wx.ALL, 5)

		self.m_staticText152 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"No set", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.m_staticText152.Wrap(-1)
		gSizer21.Add(self.m_staticText152, 0, wx.ALL, 5)

		self.m_staticText151 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"Latitude start", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.m_staticText151.Wrap(-1)
		self.m_staticText151.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer21.Add(self.m_staticText151, 0, wx.ALL, 5)

		self.m_staticText18 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"Not set", wx.DefaultPosition,
											wx.DefaultSize, 0)
		self.m_staticText18.Wrap(-1)
		gSizer21.Add(self.m_staticText18, 0, wx.ALL, 5)

		self.m_staticText161 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"Logitude end", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.m_staticText161.Wrap(-1)
		self.m_staticText161.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer21.Add(self.m_staticText161, 0, wx.ALL, 5)

		self.m_staticText162 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"Not set", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.m_staticText162.Wrap(-1)
		gSizer21.Add(self.m_staticText162, 0, wx.ALL, 5)

		self.m_staticText171 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"Latitude end", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.m_staticText171.Wrap(-1)
		self.m_staticText171.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer21.Add(self.m_staticText171, 0, wx.ALL, 5)

		self.m_staticText172 = wx.StaticText(sbSizer10.GetStaticBox(), wx.ID_ANY, u"Not set", wx.DefaultPosition,
											 wx.DefaultSize, 0)
		self.m_staticText172.Wrap(-1)
		gSizer21.Add(self.m_staticText172, 0, wx.ALL, 5)

		sbSizer10.Add(gSizer21, 1, wx.EXPAND, 5)

		bSizer14.Add(sbSizer10, 1, wx.EXPAND, 5)

		sbSizer12 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Crop coordinate"), wx.VERTICAL)

		gSizer3 = wx.GridSizer(0, 2, 0, 0)

		self.m_staticText14 = wx.StaticText(sbSizer12.GetStaticBox(), wx.ID_ANY, u"Longitude start", wx.DefaultPosition,
											wx.DefaultSize, 0)
		self.m_staticText14.Wrap(-1)
		self.m_staticText14.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer3.Add(self.m_staticText14, 0, wx.ALL, 5)

		self.m_textCtrl14 = wx.TextCtrl(sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
										wx.DefaultSize, 0)
		gSizer3.Add(self.m_textCtrl14, 0, wx.ALL | wx.EXPAND, 5)

		self.m_staticText15 = wx.StaticText(sbSizer12.GetStaticBox(), wx.ID_ANY, u"Latitude start", wx.DefaultPosition,
											wx.DefaultSize, 0)
		self.m_staticText15.Wrap(-1)
		self.m_staticText15.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer3.Add(self.m_staticText15, 0, wx.ALL, 5)

		self.m_textCtrl15 = wx.TextCtrl(sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
										wx.DefaultSize, 0)
		gSizer3.Add(self.m_textCtrl15, 0, wx.ALL | wx.EXPAND, 5)

		self.m_staticText16 = wx.StaticText(sbSizer12.GetStaticBox(), wx.ID_ANY, u"Logitude end", wx.DefaultPosition,
											wx.DefaultSize, 0)
		self.m_staticText16.Wrap(-1)
		self.m_staticText16.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer3.Add(self.m_staticText16, 0, wx.ALL, 5)

		self.m_textCtrl16 = wx.TextCtrl(sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
										wx.DefaultSize, 0)
		gSizer3.Add(self.m_textCtrl16, 0, wx.ALL | wx.EXPAND, 5)

		self.m_staticText17 = wx.StaticText(sbSizer12.GetStaticBox(), wx.ID_ANY, u"Latitude end", wx.DefaultPosition,
											wx.DefaultSize, 0)
		self.m_staticText17.Wrap(-1)
		self.m_staticText17.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		gSizer3.Add(self.m_staticText17, 0, wx.ALL, 5)

		self.m_textCtrl17 = wx.TextCtrl(sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
										wx.DefaultSize, 0)
		gSizer3.Add(self.m_textCtrl17, 0, wx.ALL | wx.EXPAND, 5)

		sbSizer12.Add(gSizer3, 1, wx.EXPAND, 5)

		bSizer14.Add(sbSizer12, 1, wx.EXPAND, 5)

		bSizer10.Add(bSizer14, 1, wx.EXPAND, 5)

		bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button61 = wx.Button(self, wx.ID_ANY, u"START CROP", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button61.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))
		self.m_button61.SetBackgroundColour(wx.Colour(255, 128, 0))

		bSizer81.Add(self.m_button61, 0, wx.ALL, 5)

		self.m_button10 = wx.Button(self, wx.ID_ANY, u"START CORRECTION", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button10.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

		bSizer81.Add(self.m_button10, 0, wx.ALL, 5)

		bSizer10.Add(bSizer81, 0, wx.EXPAND, 5)

		bSizer2.Add(bSizer10, 1, wx.EXPAND, 5)

		bSizer9 = wx.BoxSizer(wx.VERTICAL)

		sbSizer6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Correction"), wx.VERTICAL)

		bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

		sbSizer7 = wx.StaticBoxSizer(wx.StaticBox(sbSizer6.GetStaticBox(), wx.ID_ANY, u"RED"), wx.VERTICAL)

		self.m_bitmap4 = wx.StaticBitmap(sbSizer7.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
										 wx.Size(250, 250), 0)
		self.m_bitmap4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		sbSizer7.Add(self.m_bitmap4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		self.m_buttonSave = wx.Button(sbSizer7.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize,
									  0)
		self.m_buttonSave.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))
		self.m_buttonSave.SetBackgroundColour(wx.Colour(128, 255, 128))
		self.m_buttonSave.SetMaxSize(wx.Size(250, -1))

		bSizer7.Add(self.m_buttonSave, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

		sbSizer7.Add(bSizer7, 1, wx.EXPAND, 5)

		bSizer16.Add(sbSizer7, 1, wx.EXPAND, 5)

		sbSizer71 = wx.StaticBoxSizer(wx.StaticBox(sbSizer6.GetStaticBox(), wx.ID_ANY, u"NIR"), wx.VERTICAL)

		self.m_bitmap41 = wx.StaticBitmap(sbSizer71.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
										  wx.Size(250, 250), 0)
		self.m_bitmap41.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		sbSizer71.Add(self.m_bitmap41, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		bSizer72 = wx.BoxSizer(wx.VERTICAL)

		self.m_buttonSave1 = wx.Button(sbSizer71.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize,
									   0)
		self.m_buttonSave1.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))
		self.m_buttonSave1.SetBackgroundColour(wx.Colour(128, 255, 128))
		self.m_buttonSave1.SetMaxSize(wx.Size(250, -1))

		bSizer72.Add(self.m_buttonSave1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

		sbSizer71.Add(bSizer72, 1, wx.EXPAND, 5)

		bSizer16.Add(sbSizer71, 1, wx.EXPAND, 5)

		sbSizer6.Add(bSizer16, 1, wx.EXPAND, 5)

		bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_button8 = wx.Button(sbSizer6.GetStaticBox(), wx.ID_ANY, u"START NDVI", wx.DefaultPosition,
								   wx.DefaultSize, 0)
		self.m_button8.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))
		self.m_button8.SetBackgroundColour(wx.Colour(255, 128, 0))

		bSizer17.Add(self.m_button8, 0, wx.ALL, 5)

		sbSizer6.Add(bSizer17, 0, wx.EXPAND, 5)

		bSizer9.Add(sbSizer6, 0, wx.EXPAND, 5)

		sbSizer8 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"NDVI Result"), wx.VERTICAL)

		gbSizer1 = wx.GridBagSizer(0, 0)
		gbSizer1.SetFlexibleDirection(wx.BOTH)
		gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_bitmap11 = wx.StaticBitmap(sbSizer8.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
										  wx.Size(250, 250), 0)
		self.m_bitmap11.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

		gbSizer1.Add(self.m_bitmap11, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

		self.m_button9 = wx.Button(sbSizer8.GetStaticBox(), wx.ID_ANY, u"SAVE", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button9.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))
		self.m_button9.SetBackgroundColour(wx.Colour(128, 255, 128))

		gbSizer1.Add(self.m_button9, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		sbSizer8.Add(gbSizer1, 1, wx.EXPAND, 5)

		bSizer9.Add(sbSizer8, 1, wx.EXPAND, 5)

		bSizer2.Add(bSizer9, 1, wx.EXPAND, 5)

		self.SetSizer(bSizer2)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_filePickerRed.Bind(wx.EVT_FILEPICKER_CHANGED, self.filePickerRedChanged)
		self.m_button5.Bind(wx.EVT_BUTTON, self.onSaveRed)
		self.m_filePickerNir.Bind(wx.EVT_FILEPICKER_CHANGED, self.filePickerNirChanged)
		self.m_button6.Bind(wx.EVT_BUTTON, self.onSaveNir)
		self.m_filePicker3.Bind(wx.EVT_FILEPICKER_CHANGED, self.importMtlChanged)
		self.m_button61.Bind(wx.EVT_BUTTON, self.onStartCrop)
		self.m_button10.Bind(wx.EVT_BUTTON, self.onStartCorrection)
		self.m_buttonSave.Bind(wx.EVT_BUTTON, self.onSaveCorrectionRed)
		self.m_buttonSave1.Bind(wx.EVT_BUTTON, self.onSaveCorrectionNir)
		self.m_button8.Bind(wx.EVT_BUTTON, self.onStartNDVI)
		self.m_button9.Bind(wx.EVT_BUTTON, self.onSaveResult)

		self.ndvi = NDVI()
		self.ndvi.SetOnProcessFinishListener(self)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def filePickerRedChanged( self, event ):
		path = event.GetPath()
		self.ndvi.OpenB4File(path)
		if self.ndvi.isOpenB4:
			bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
			image = wx.Bitmap.ConvertToImage(bitmap)
			scaledImage = image.Scale(250, 250, wx.IMAGE_QUALITY_HIGH)
			bitmap = wx.Bitmap(scaledImage)
			self.m_bitmap2.SetBitmap(bitmap)
			if self.ndvi.open_B4:
				self.showMessage("Band 4 image loaded successfully")
			else:
				self.showMessageError("Band 4 image failed to loaded")
		else:
			self.showMessageError("Failed\n\nFailed to load file\nCaused by the file loaded are not band 4 image")
		event.Skip()
	
	def onSaveRed( self, event ):
		if self.ndvi.isCropped:
			saveFileDialog = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*tif)|*.tif',
										   wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

			if (saveFileDialog.ShowModal() == wx.ID_OK):
				path = saveFileDialog.GetPath()
				self.ndvi.SaveRed(path)
				self.showMessage("File has been saved.")
		else:
			self.showMessageError("Failed to save file\n\nCaused by image not cropped before. Try run crop image before save")
		event.Skip()
	
	def filePickerNirChanged( self, event ):
		path = event.GetPath()
		self.ndvi.OpenB5File(path)
		if self.ndvi.isOpenB5:
			bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
			image = wx.Bitmap.ConvertToImage(bitmap)
			scaledImage = image.Scale(250, 250, wx.IMAGE_QUALITY_HIGH)
			bitmap = wx.Bitmap(scaledImage)
			self.m_bitmap3.SetBitmap(bitmap)
			if self.ndvi.open_B5:
				self.showMessage("Band 5 image loaded successfully")
			else:
				self.ndvi.listener.showMessageError("Band 5 image failed to loaded")
		else:
			self.showMessageError("Failed\n\nFailed to load image\nCaused by the file loaded is not band 5 image")
		event.Skip()
	
	def onSaveNir( self, event ):
		if self.ndvi.isCropped:
			saveFileDialog = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*tif)|*.tif',
										   wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

			if (saveFileDialog.ShowModal() == wx.ID_OK):
				path = saveFileDialog.GetPath()
				self.ndvi.SaveNir(path)
				self.showMessage("File has been saved.")
		else:
			self.showMessageError("Failed to save file\n\nCaused by image not cropped before. Try run crop image before save")
		event.Skip()
	
	def importMtlChanged( self, event ):
		path = event.GetPath()
		self.ndvi.OpenMtlFile(path)
		self.m_staticText152.SetLabel(str(self.ndvi.lonStartDefault))
		self.m_staticText18.SetLabel(str(self.ndvi.latStartDefault))
		self.m_staticText162.SetLabel(str(self.ndvi.lonEndDefault))
		self.m_staticText172.SetLabel(str(self.ndvi.latEndDefault))
		self.Layout()
		event.Skip()
	
	def onStartCrop( self, event ):
		if self.ndvi.isMtl or (self.ndvi.isOpenB4 and self.ndvi.isOpenB5):
			lonStart = self.m_textCtrl14.GetValue()
			latStart = self.m_textCtrl15.GetValue()
			lonEnd = self.m_textCtrl16.GetValue()
			latEnd = self.m_textCtrl17.GetValue()

			print(lonStart)
			print(latStart)
			print(lonEnd)
			print(latEnd)

			self.ndvi.SetCropCoordinate(lonStart, lonEnd, latStart, latEnd)
			self.ndvi.CropImage()
		else:
			self.showMessageError("Failed\n\nFailed to crop image\nCaused by image not loaded or file mtl not imported")
		event.Skip()
	
	def onStartCorrection( self, event ):
		self.ndvi.StartCorrection()
		if self.ndvi.isCorrection == False:
			self.showMessageError("Correction failed\n\nCaused by image not cropped before")
		event.Skip()
	
	def onSaveCorrectionRed( self, event ):
		if self.ndvi.isCorrection:
			saveFileDialog = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*tif)|*.tif',
										   wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

			if (saveFileDialog.ShowModal() == wx.ID_OK):
				path = saveFileDialog.GetPath()
				self.ndvi.SaveCorrectionRed(path)
				self.showMessage("File has been saved.")
			else:
				self.showMessageError("Aborted")
		else:
			self.showMessageError("Failed to save file\n\nCaused by image not cropped bfore. Try run correction image before save")
		event.Skip()
	
	def onSaveCorrectionNir( self, event ):
		if self.ndvi.isCorrection:
			saveFileDialog = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*tif)|*.tif',
										   wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

			if (saveFileDialog.ShowModal() == wx.ID_OK):
				path = saveFileDialog.GetPath()
				self.ndvi.SaveCorrectionNir(path)
				self.showMessage("File has been saved.")
			else:
				self.showMessageError("Aborted")
		else:
			self.showMessageError("Failed to save file\n\nCaused by image not cropped before. Try run correction image before save")
		event.Skip()
	
	def onStartNDVI( self, event ):
		if self.ndvi.isCorrection:
			self.ndvi.StartNDVI()
		else:
			self.showMessageError("Failed to start NDVI\n\nCaused by image not corrected before")
		event.Skip()
	
	def onSaveResult( self, event ):
		if self.ndvi.isNdvi:
			saveFileDialog = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*tif)|*.tif',
										   wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

			if (saveFileDialog.ShowModal() == wx.ID_OK):
				path = saveFileDialog.GetPath()
				self.ndvi.SaveResult(path)
				self.showMessage("File has been saved.")
			else:
				self.showMessageError("Aborted")
		else:
			self.showMessageError("Failed to save file\n\nCaused by NDVI result not found. Try run NDVI before save the file")
		event.Skip()
	
	def showMessage(self, message):
		dialog = wx.MessageDialog(None, message, "Info", wx.OK | wx.ICON_INFORMATION)
		dialog.ShowModal()

	def showMessageError(self, message):
		dialog = wx.MessageDialog(None, message, "Error", wx.OK | wx.ICON_ERROR)
		dialog.ShowModal()

	def onCropFinish(self, red, nir):
		red_image = self.convertToImage(red, False)
		nir_image = self.convertToImage(nir, False)
		print(red)
		print(nir)

		self.m_bitmap2.SetBitmap(wx.Bitmap(red_image))
		self.m_bitmap3.SetBitmap(wx.Bitmap(nir_image))

		self.showMessage("Image cropped successfuly")

		frame.Layout()

	def onCorrectionFinish(self, red, nir):
		red_image = self.convertToImage(red, False)
		nir_image = self.convertToImage(nir, False)
		print(red)
		print(nir)

		self.m_bitmap4.SetBitmap(wx.Bitmap(red_image))
		self.m_bitmap41.SetBitmap(wx.Bitmap(nir_image))

		self.showMessage("Image corrected successfuly")

		frame.Layout()

	def onNDVIFinish(self, result):
		image = self.convertToImage(result, True)
		print ('result ', image)
		self.m_bitmap11.SetBitmap(wx.Image.ConvertToBitmap(image))

		self.showMessage("NDVI successfuly")

		frame.Layout()


	def convertToImage(self, array, isfloat):
		if isfloat:
			rgb = array * 255
		else:
			rgb = array / 255

		pilImage = Image.fromarray(rgb).convert('RGB')
		image = wx.EmptyImage(pilImage.size[0], pilImage.size[1])
		image.SetData(pilImage.tobytes())

		H = image.GetHeight()
		W = image.GetWidth()
		newH = 250
		newW = 250
		if (W > H):
			newH = 250 * H / W
		else:
			newW = 250 * W / H

		image = image.Scale(newW, newH)
		return image




#Mandatory in wx, create an app, False stand for not deteriction stdin/stdout
#refer manual for detail
app = wx.App(False)

#create an object of MyFrame2
frame = MyFrame1(None)
#show the frame
frame.Show(True)
#start the application
app.MainLoop()