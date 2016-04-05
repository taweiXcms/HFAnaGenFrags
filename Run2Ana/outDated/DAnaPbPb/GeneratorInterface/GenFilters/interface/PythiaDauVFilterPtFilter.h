#ifndef PYTHIADAUVFILTERPTFILTER_h
#define PYTHIADAUVFILTERPTFILTER_h
// -*- C++ -*-
//
// Package:    PythiaDauVFilterPtFilter
// Class:      PythiaDauVFilterPtFilter
// 
/**\class PythiaDauVFilterPtFilter PythiaDauVFilterPtFilter.cc 

 Description: Filter events using MotherId and ChildrenIds infos

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Daniele Pedrini
// Modified: Ta-Wei Wang
//         Created:  Dec 25 2015
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"


//
// class decleration
//
namespace edm {
  class HepMCProduct;
}

class PythiaDauVFilterPtFilter : public edm::EDFilter {
 public:
  explicit PythiaDauVFilterPtFilter(const edm::ParameterSet&);
  ~PythiaDauVFilterPtFilter();
  
  
  virtual bool filter(edm::Event&, const edm::EventSetup&);
 private:
  int fVerbose;  
  edm::EDGetTokenT<edm::HepMCProduct> token_;
  std::vector<int> dauIDs;
  int particleID;
  int motherID;
  double motherPt;
  double motherMaxEta;
  double motherMinEta;
  int motherStatus;
  bool chargeconju; 
  int ndaughters;
  std::vector<double> minptcut;
  double maxptcut;
  std::vector<double> minetacut;
  std::vector<double> maxetacut;
  double particlePt;
  double particleMaxEta;
  double particleMinEta;
  int particleStatus;
};
#define PYCOMP pycomp_
extern "C" {
  int PYCOMP(int& ip);
} 
#endif
