import { TestBed } from '@angular/core/testing';

import { ScrapedataService } from './scrapedata.service';

describe('ScrapedataService', () => {
  let service: ScrapedataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ScrapedataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
