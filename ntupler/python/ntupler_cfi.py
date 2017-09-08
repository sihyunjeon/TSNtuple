import FWCore.ParameterSet.Config as cms

process.ntuplerBase = cms.EDAnalyzer("ntupler",
	OfflineMuon = cms.untracked.InputTag("muons"),
	OfflineVertex = cms.untracked.InputTag("offlinePrimaryVertices"),
	TriggerResults = cms.untracked.InputTag("TriggerResults::HLT"),
	TriggerEvent = cms.untracked.InputTag("hltTriggerSummaryAOD::HLT"),
	L3Muon = cms.untracked.InputTag("hltIterL3MuonCandidates"),
	L2Muon = cms.untracked.InputTag("hltL2MuonCandidates"),
	# L1Muon = cms.untracked.InputTag("gmtStage2Digis", "Muon", "RECO"), # -- if not HLT re-run -- #
	L1Muon = cms.untracked.InputTag("hltGmtStage2Digis", "Muon"), # -- if HLT re-run --#

	TkMuon = cms.untracked.InputTag("hltHighPtTkMuonCands"),
	ChargedIsoDep = cms.untracked.InputTag("hltMuonTkRelIsolationCut0p07Map", "trkIsoDeposits", "REHLT"),
	NeutralIsoDep = cms.untracked.InputTag("hltMuonHcalM2RegPFClusterIsoForMuons"),
	PhotonIsoDep = cms.untracked.InputTag("hltMuonEcalMFPFClusterIsoForMuons"),
	Rho = cms.untracked.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
	OfflineRho = cms.untracked.InputTag("fixedGridRhoFastjetAllCalo"),

	RhoECAL = cms.untracked.InputTag("hltFixedGridRhoFastjetECALMFForMuons"),
	RhoHCAL = cms.untracked.InputTag("hltFixedGridRhoFastjetHCAL"),

	OfflineECALPFIso03 = cms.untracked.InputTag("muonEcalPFClusterIsolationProducer03"),
	OfflineHCALPFIso03 = cms.untracked.InputTag("muonHcalPFClusterIsolationProducer03"),
	OfflineECALPFIso04 = cms.untracked.InputTag("muonEcalPFClusterIsolationProducer04"),
	OfflineHCALPFIso04 = cms.untracked.InputTag("muonHcalPFClusterIsolationProducer04"),

	LumiScaler = cms.untracked.InputTag("scalersRawToDigi"),
	PUSummaryInfo = cms.untracked.InputTag("addPileupInfo"),
	GenEventInfo = cms.untracked.InputTag("generator"),
	GenParticle = cms.untracked.InputTag("genParticles"),
)