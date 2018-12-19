import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
						 pythiaPylistVerbosity = cms.untracked.int32(0),
						 pythiaHepMCVerbosity = cms.untracked.bool(False),
						 comEnergy = cms.double(5020.0),
						 maxEventsToPrint = cms.untracked.int32(0),
						 ExternalDecays = cms.PSet(
							 EvtGen130 = cms.untracked.PSet(
								 decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
								 particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
								 user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Onia_mumu_withX3872.dec'),
								 list_forced_decays = cms.vstring('myX3872NoRes'),
								 operates_on_particles = cms.vint32()
							 ),
							 parameterSets = cms.vstring('EvtGen130')
						 ),
                         PythiaParameters = cms.PSet(
							 pythia8CommonSettingsBlock,
							 pythia8CUEP8M1SettingsBlock,
							 processParameters = cms.vstring(
								 # 'HardQCD:all = on',
								 'Charmonium:states(3PJ) = 20443',
								 'Charmonium:O(3PJ)[3P0(1)] = 0.05',
								 'Charmonium:O(3PJ)[3S1(8)] = 0.0031',
								 'Charmonium:gg2ccbar(3PJ)[3PJ(1)]g = on',
								 'Charmonium:qg2ccbar(3PJ)[3PJ(1)]q = on',
								 'Charmonium:qqbar2ccbar(3PJ)[3PJ(1)]g = on',
								 'Charmonium:gg2ccbar(3PJ)[3S1(8)]g = on',
								 'Charmonium:qg2ccbar(3PJ)[3S1(8)]q = on',
								 'Charmonium:qqbar2ccbar(3PJ)[3S1(8)]g = on',
								 '20443:m0=3.87156',
								 '20443:mWidth=0.0023',
								 'PhaseSpace:pTHatMin = 50.',
							 ),
        parameterSets = cms.vstring('pythia8CommonSettings',
									'pythia8CUEP8M1Settings',
									'processParameters',
								)
        )
                         )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########
mumugenfilter = cms.EDFilter("MCParticlePairFilter",
							 Status = cms.untracked.vint32(1, 1),
							 MinPt = cms.untracked.vdouble(0.5, 0.5),
							 MinP = cms.untracked.vdouble(0., 0.),
							 MaxEta = cms.untracked.vdouble(2.5, 2.5),
							 MinEta = cms.untracked.vdouble(-2.5, -2.5),
							 MinInvMass = cms.untracked.double(2.0),
							 MaxInvMass = cms.untracked.double(4.0),
							 ParticleCharge = cms.untracked.int32(-1),
							 ParticleID1 = cms.untracked.vint32(13),
							 ParticleID2 = cms.untracked.vint32(13)
)

X3872JpsiDaufilter = cms.EDFilter("PythiaMomDauFilter",
								  ParticleID = cms.untracked.int32(20443),
								  MomMinPt = cms.untracked.double(0.),
								  MomMinEta = cms.untracked.double(-2.4),
								  MomMaxEta = cms.untracked.double(2.4),
								  DaughterIDs = cms.untracked.vint32(443, 211, -211),
								  NumberDaughters = cms.untracked.int32(3),
								  NumberDescendants = cms.untracked.int32(0),
)

ProductionFilterSequence = cms.Sequence(generator*mumugenfilter*X3872JpsiDaufilter)
