#include <TagProbe/MakeHist_TnP_IsoMu27.h>

void MakeHist_TnP_IsoMu27_Menu3p2()
{
	HistProducer* producer = new HistProducer();
	producer->SetOutputFileName( "ROOTFile_MakeHist_TnP_IsoMu27_Menu3p2.root" );

	TString DataPath = gSystem->Getenv("KP_DATA_PATH");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics1_Run2017Fv1/ntuple_*.root");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics2_Run2017Fv1/ntuple_*.root");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics3_Run2017Fv1/ntuple_*.root");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics4_Run2017Fv1/ntuple_*.root");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics5_Run2017Fv1/ntuple_*.root");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics6_Run2017Fv1/ntuple_*.root");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics7_Run2017Fv1/ntuple_*.root");
	producer->AddDataPath(DataPath+"/92X/TSntuple_v20171109_Menu3p2_EphemeralHLTPhysics8_Run2017Fv1/ntuple_*.root");
	producer->Produce();
	// producer->AddDataPath("");
	// producer->AddDataPath("");
}