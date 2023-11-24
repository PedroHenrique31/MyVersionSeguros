import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApoliceDetailComponent } from './apolice-detail.component';

describe('ApoliceDetailComponent', () => {
  let component: ApoliceDetailComponent;
  let fixture: ComponentFixture<ApoliceDetailComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ApoliceDetailComponent]
    });
    fixture = TestBed.createComponent(ApoliceDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
