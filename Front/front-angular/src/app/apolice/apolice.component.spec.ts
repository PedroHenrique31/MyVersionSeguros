import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ApoliceComponent } from './apolice.component';

describe('ApoliceComponent', () => {
  let component: ApoliceComponent;
  let fixture: ComponentFixture<ApoliceComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ApoliceComponent]
    });
    fixture = TestBed.createComponent(ApoliceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
