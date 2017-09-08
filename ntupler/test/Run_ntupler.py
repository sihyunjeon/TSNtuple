import FWCore.ParameterSet.Config as cms

process = cms.Process("ntupler")

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring('file:outputFULL.root'),
	secondaryFileNames = cms.untracked.vstring(),
	# lumisToProcess = cms.untracked.VLuminosityBlockRange('258158:1-258158:1786'),
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = '92X_dataRun2_HLT_v7'

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')

# -- ntupler -- #
from TriggerStudyNtuple.ntupler.ntupler_cfi import *

process.ntupler = ntuplerBase.clone()
process.ntupler.OfflineMuon = cms.untracked.InputTag("muons")
process.ntupler.L3Muon = cms.untracked.InputTag("hltIterL3MuonCandidates")
process.ntupler.L2Muon = cms.untracked.InputTag("hltL2MuonCandidates")
# process.ntupler.L1Muon = cms.untracked.InputTag("hltGmtStage2Digis", "Muon") # -- after HLT re-run -- #
process.ntupler.L1Muon = cms.untracked.InputTag("hltGtStage2Digis", "Muon") # -- after HLT re-run -- #
# process.ntupler.L1Muon = cms.untracked.InputTag("gmtStage2Digis", "Muon", "RECO") # -- without HLT re-run -- #

process.mypath = cms.Path(process.ntupler)

process.TFileService = cms.Service("TFileService",
	fileName = cms.string("ntuple.root"),
	closeFileFast = cms.untracked.bool(False),
	)

process.MessageLogger = cms.Service( "MessageLogger",
	destinations = cms.untracked.vstring("cerr"),
	cerr = cms.untracked.PSet( threshold = cms.untracked.string('ERROR'), ),
	)