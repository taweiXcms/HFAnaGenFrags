import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
                         ExternalDecays = cms.PSet(
                             EvtGen = cms.untracked.PSet(
                                 use_default_decay = cms.untracked.bool(False),
                                 use_internal_pythia = cms.untracked.bool(False),
                                 decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
                                 particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
                                 user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/D0_Kpi.dec'),
                                 list_forced_decays = cms.vstring('myD0', 'myanti-D0'),
                                 operates_on_particles = cms.vint32(0)
                             ),
                             parameterSets = cms.vstring('EvtGen')
                         ),
                         comEnergy = cms.double(5020.0),
                         crossSection = cms.untracked.double(2.035e-01),
                         filterEfficiency = cms.untracked.double(9.132e-02),
                         maxEventsToPrint = cms.untracked.int32(-1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         pythiaPylistVerbosity = cms.untracked.int32(False),
                         PythiaParameters = cms.PSet(pythiaUESettingsBlock,
                                                     processParameters = cms.vstring('MSEL=1   ! QCD hight pT processes',
                                                                                     'CKIN(3)= 5  ! minimum pt hat for hard interactions',
                                                                                     ),
                                                     parameterSets = cms.vstring('pythiaUESettings',
                                                                                 'processParameters',
                                                                                 )
                                                     )
                         )

D0filter = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.4, 2.4),
    MinEta = cms.untracked.vdouble(-2.4, -2.4),
    MinPt = cms.untracked.vdouble(5.0, 5.0),
    ParticleID = cms.untracked.vint32(421, -421)
)

ProductionFilterSequence = cms.Sequence(generator*D0filter)



