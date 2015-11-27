# Auto generated configuration file
# using: 
# Revision: 1.381.2.13 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/HI/PyquenMix_DYtoMuMu_M_30_TuneZ2_embedHIJING_BptpJpsiKp5TeV02_cfi.py -n 1 -s GEN,SIM,DIGI,L1,HLT:PIon,L1Reco,RECO --conditions auto:mc --geometry Extended --datatier GEN-SIM-DIGI-RECO --eventcontent=RECODEBUG --filein=input.root --processName HISIGNAL --no_exec --himix --scenario HeavyIons --beamspot Realistic8TeVCollisionPPbBoost
import FWCore.ParameterSet.Config as cms

process = cms.Process('HISIGNAL')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiEventMixing_cff')
process.load('Configuration.Geometry.GeometryExtendedReco_cff')
process.load('Configuration.Geometry.GeometryExtended_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.HiGenCommon.VtxSmearedRealisticPPbBoost8TeVCollision_cff')
process.load('SimGeneral.MixingModule.himixGEN_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('SimGeneral.MixingModule.himixSIMExtended_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('SimGeneral.MixingModule.himixDIGI_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_PIon_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
#process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(5)
#   input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
   secondaryFileNames = cms.untracked.vstring(),
   fileNames = cms.untracked.vstring(
#      'file:E6C7EEFE-E567-E211-BFD6-00A0D1E952FC.root'
   ),
   inputCommands = cms.untracked.vstring('drop *', 
       'keep *_generator_*_*', 
       'keep *_g4SimHits_*_*'),
   dropDescendantsOfDroppedBranches = cms.untracked.bool(False)
)

process.options = cms.untracked.PSet(
       wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
   version = cms.untracked.string('$Revision: 1.381.2.13 $'),
   annotation = cms.untracked.string('Configuration/Generator/python/HI/PyquenMix_DYtoMuMu_M_30_TuneZ2_embedHIJING_BptpJpsiKp5TeV02_cfi.py nevts:1'),
   name = cms.untracked.string('PyReleaseValidation')
)

# seeds
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()

print process.RandomNumberGeneratorService.dumpConfig()

# generator

from Configuration.Generator.PyquenDefaultSettings_cff import *
from Configuration.Generator.PythiaUEZ2Settings_cfi import *

process.hiSignal = cms.EDFilter("PyquenGeneratorFilter",
       filterType = cms.untracked.string("BpCandGenEvtSelector"),
       #filterType = cms.untracked.string("MultiCandGenEvtSelector"),
       ptMin = cms.double(0.3),
       etaMax = cms.double(3.0),
       pdg = cms.int32(511),
       dau2pdg = cms.int32(313),
       dau2dau1pdg = cms.int32(211),
       dau2dau2pdg = cms.int32(321),
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
                       #user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bu_JpsiK.dec'),
                       user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bd_JpsiKstar_mumuKpi.dec'),
                       list_forced_decays = cms.vstring('MyB0','Myanti-B0'),
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

process.bfilter = cms.EDFilter(
       "PythiaFilter",
       moduleLabel = cms.string("hiSignal"),
       MaxEta = cms.untracked.double(5.0),
       MinEta = cms.untracked.double(-5.0),
       ParticleID = cms.untracked.int32(521)
)

process.jpsifilter = cms.EDFilter(
       "PythiaDauVFilter",
       moduleLabel = cms.string("hiSignal"),
       verbose = cms.untracked.int32(30),
       NumberDaughters = cms.untracked.int32(2),
       MotherID = cms.untracked.int32(521),
       ParticleID = cms.untracked.int32(443),
       DaughterIDs = cms.untracked.vint32(13,-13),
       MinPt = cms.untracked.vdouble(0.0,0.0),
       MinEta = cms.untracked.vdouble(-5.0,-5.0),
       MaxEta = cms.untracked.vdouble(5.0,5.0)
)

process.kfilter = cms.EDFilter(
       "PythiaDauVFilter",
       moduleLabel = cms.string("hiSignal"),
       verbose = cms.untracked.int32(30),
       NumberDaughters = cms.untracked.int32(2),
       MotherID = cms.untracked.int32(0),
       ParticleID = cms.untracked.int32(521),
       DaughterIDs = cms.untracked.vint32(443,321),
       MinPt = cms.untracked.vdouble(0.,0.0),
       MinEta = cms.untracked.vdouble(-5.0,-5.0),
       MaxEta = cms.untracked.vdouble(5.0,5.0)
)
#process.ProductionFilterSequence = cms.Sequence(process.hiGenParticles*process.bfilter*process.jpsifilter*process.kfilter)
process.ProductionFilterSequence = cms.Sequence(process.hiSignal)

# Output definition

process.RECODEBUGoutput = cms.OutputModule("PoolOutputModule",
   splitLevel = cms.untracked.int32(0),
   eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
   outputCommands = process.RECODEBUGEventContent.outputCommands,
   fileName = cms.untracked.string(
      'PyquenMix_embedHIJING_Bd2JpsiKstar_5TeV.root'),
   dataset = cms.untracked.PSet(
       filterName = cms.untracked.string(''),
       dataTier = cms.untracked.string('GEN-SIM-DIGI-RECO')
   ),
   SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring('generation_step')
   )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'STARTHI53_V17::All', '')

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen_himix)
#process.generation_step = cms.Path(process.randomEngineStateProducer+process.matchVtx+process.hiGenParticles)

process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
#process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)
process.reconstruction_step = cms.Path(process.reconstruction)

process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECODEBUGoutput_step = cms.EndPath(process.RECODEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECODEBUGoutput_step])
# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# special treatment in case of production filter sequence
for path in process.paths:
   getattr(process,path)._seq = process.ProductionFilterSequence*getattr(process,path)._seq
#    getattr(process,path)._seq = getattr(process,path)._seq*process.ProductionFilterSequence

# End of customisation functions

