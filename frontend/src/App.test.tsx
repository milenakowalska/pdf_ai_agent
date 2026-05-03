import { render, screen } from '@testing-library/react';
import App from './App';

test('renders homepage', () => {
  render(<App />);
  const homepage = screen.getByText(/Homepage/i);
  expect(homepage).toBeInTheDocument();
});
