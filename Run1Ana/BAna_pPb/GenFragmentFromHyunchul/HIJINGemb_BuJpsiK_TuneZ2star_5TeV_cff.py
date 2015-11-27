import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PyquenDefaultSettings_cff import *
from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

hiSignal = cms.EDFilter("PyquenGeneratorFilter",
        filterType = cms.untracked.string("BpCandGenEvtSelector"),
	#filterType = cms.untracked.string("MultiCandGenEvtSelector"),
  	ptMin = cms.double(0.0),
	etaMin = cms.double(-3.0),
   	etaMax = cms.double(3.0),#from 2.5
   	pdg = cms.int32(521),
        status = cms.int32(1),
        minimumCandidates = cms.int32(1),
        comEnergy = cms.double(5023.0),
        aBeamTarget = cms.double(208.0),
        protonSide = cms.untracked.int32(2),
        qgpInitialTemperature = cms.double(1.0),
        qgpProperTimeFormation = cms.double(0.1),
        hadronFreezoutTemperature = cms.double(0.14),
        doRadiativeEnLoss = cms.bool(True),
        doCollisionalEnLoss = cms.bool(False),
        qgpNumQuarkFlavor = cms.int32(0),
        numQuarkFlavor = cms.int32(0),
        doIsospin = cms.bool(True),
        angularSpectrumSelector = cms.int32(0),
        embeddingMode = cms.bool(True),
        backgroundLabel = cms.InputTag("generator"),
        doQuench = cms.bool(False),
        bFixed = cms.double(0.0),
        cFlag = cms.int32(0),
        bMin = cms.double(0.0),
        bMax = cms.double(0.0),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        pythiaHepMCVerbosity = cms.untracked.bool(True),
        maxEventsToPrint = cms.untracked.int32(0),
        ExternalDecays = cms.PSet(
		EvtGen = cms.untracked.PSet(
                        operates_on_particles =cms.vint32(0),
                        use_default_decay = cms.untracked.bool(False),
                        decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
                        particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
                        user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bu_JpsiK.dec'),
                        list_forced_decays = cms.vstring('MyB+','MyB-'),
                ),
                parameterSets = cms.vstring('EvtGen')
        ),
        PythiaParameters = cms.PSet(
                pythiaUESettingsBlock,
                bbbarSettings = cms.vstring('MSEL = 1'),
                parameterSets = cms.vstring('pythiaUESettings',
                                'bbbarSettings')
        )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string
    ('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/PYTHIA6_Bu2JpsiK_TuneZ2_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('B+ -> Jpsi K+ at 5TeV for embedding on HIJING')
    )
ProductionFilterSequence = cms.Sequence(hiSignal)
